package lesson10;

public class StringCheese {
    public static String reversed(String words) {
        String reversed = "";
        for (int x = words.length() - 1; x >= 0; x--) {
            reversed += words.charAt(x);
        }
        return reversed;
    }

    public static boolean Palindrome(String words) {
        words = words.trim().toLowerCase();
        String without = "";
        for (int i = 0; i < words.length(); i++) {
            if ("abcdefghijklmnopqrstuvwxyz0123456789".contains(words.substring(i, i + 1))) {
                without += words.charAt(i);
            }
        }
        return without.equals(reversed(without));
    }

    private static String piggo(String word) {
        String endWord = "";
        if (!"aeiouAEIOU".contains(word.substring(0, 1))) {
            endWord = word + "ay";
        }
        for (int i = 0; i < word.length(); i++) {
            if ("aeiouAEIOU".contains(word.toLowerCase().substring(i, i + 1))) {
                if (i == 0) {
                    endWord = word + "yay";
                    break;
                } else {

                    endWord = word.substring(i) + word.substring(0, i).toLowerCase() + "ay";
                    if (word.matches("[A-Z].*")) {
                        //System.out.println(word);
                        endWord = endWord.substring(0, 1).toUpperCase() + endWord.substring(1);
                    } else {
                        // System.out.printf("\n failed : %s", word);
                    }
                    break;
                }
            }
        }
        return endWord.substring(0, 1) + endWord.substring(1);//i dont know what this does, i think it does nothing but im keeping because i dont want to break my code
    }

    public static String piggy(String sen) {
        sen = sen.trim();
        //sen = sen.toLowerCase();
        //sen = sen.toLowerCase();
        sen = sen.replaceAll("[^a-zA-Z ]", "").replaceAll("  ", " ");

        String[] words = sen.split(" ");
        String yes = "";
        for (int w = 0; w < words.length; w++) {
            yes += piggo(words[w]) + " ";
        }
        return yes;

    }

    public static String shortTalk(String words) {
        words = words.replaceAll("(?) and ", " & ").replaceAll("(?) to ", " 2 ")
                .replaceAll("(?) for ", " 4 ").replaceAll("(?)[aeiou]", "").replaceAll("(?) y ", " U ");
        return words;
    }
}
