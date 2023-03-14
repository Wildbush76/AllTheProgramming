<?php

$function = $_POST['function'];

$log = array();

switch ($function) {

	case ('getState'):
		if (file_exists('chat.html')) {
			$lines = file('chat.html');
		}
		$log['state'] = count($lines);
		break;

	case ('update'):
		$state = $_POST['state'];
		if (file_exists('chat.html')) {
			$lines = file('chat.html');
		}
		$count = count($lines);
		if ($state == $count) {
			$log['state'] = $state;
			$log['text'] = false;

		} else {
			$text = array();
			$log['state'] = $state + count($lines) - $state;
			foreach ($lines as $line_num => $line) {
				if ($line_num >= $state) {
					$text[] = $line = str_replace("\n", "", $line);
				}

			}
			$log['text'] = $text;
		}

		break;

	case ('send'):
		date_default_timezone_set("America/Chicago");
		$reg_exUrl = "/(http|https|ftp|ftps)\:\/\/[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(\/\S*)?/";
		$message = $_POST['message'];
		$date = date("Y-m-d h:i:sa");
		$nickname = $_POST['nickname'];

		if (($message) != "\n") {
			if (preg_match($reg_exUrl, $message, $url) && strpos($message, "img") == false) {
				echo "test";
				$message = preg_replace($reg_exUrl, '<a href="' . $url[0] . '" target="_blank">' . $url[0] . '</a>', $message);
			}
			$message = str_replace("\n", " ", $message);
			if ($nickname == "Server") {
				$message = "<span class=\"server\">" . $message . "</span>";
			}

			$file1 = fopen('chat.html', 'a');
			$file2 = fopen('BACKUP.txt', 'a');
			$fullMessage = "<span class='tooltip'>" . "<span class='tooltiptext'>" . $date . "</span class=\"name\">" . $nickname . "</span>" . $message . "\n";

			fwrite($file1, $fullMessage);
			fwrite($file2, $nickname . " -> " . $message . " : " . $date . "\n");

			fclose($file1);
			fclose($file2);
		}
		break;
	case ('clear'):
		unlink("chat.html");
		break;
}

echo json_encode($log);

?>