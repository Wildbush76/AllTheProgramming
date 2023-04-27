var foo;
var output;
function setup() {
	createCanvas(1200, 500);
	if (My_pain == true) {
		foo = new p5.SpeechRec('en-US');
		foo.continuous = true;
		foo.interimResults = true;
		foo.onResult = showResult;
		foo.start();
	}
	le_bullet_image = loadImage('bullets.png');

	background(100);
	for (let abc in level1) {
		if (values1[abc] == 6) {
			T_hath.push(4)
			delayyy.push(0);
		} else if (values1[abc] == 7) {
			bstate.push(false)
		}
	}
}
keyPressed = function () {
	keys[keyCode] = true;
}
keyReleased = function () {
	keys[keyCode] = false;
}
function showResult() {
	output = foo.resultString;
	output = output.toLowerCase()
	if (output.includes('jump')) {
		y -= 2;
		g = -jumpH;
	}
	console.log(output)
}
var coliS = false;
var wait = 0;
var time_go_slow = 0;
var TSelect = 0;
var T_dubug = [];
var debug = false;
var le_bullet_image;
var ammo = [5, 4];
var player_shooty_delay = 0;
var hath = 5;
var bull = [];
var death_counter = -1;
var started = false;
var cl = true;
var right = true;
var movement_speed = 4;
var jumpH = 6;
var keys = [];
var level1 = [0, 60, 120, 180, 240, 300, 360, 480, 540, 600, 660, 720, 900, 960, 1020, 1080, 1140, 1200, 840, 780, 420, 1260, 1320, 1380, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, -9, 51, 52, 53, 54, 55, 56, 57, 58, 59, 119, 179, 239, 299, 359, 419, 479, 539, 599, 659, 719, 779, 839, 899, 959, 1019, 1079, 1139, 1500, 1560, 1499, 1439, 1379, 1319, 1259, 1199, 1476, 1477, 1479, 1480, 1481, 1482, 1483, 1484, 1478, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1261, 1262, 1263, 1264, 1265, 1202, 1321, 1322, 1323, 1324, 1325, 1385, 1386, 1326, 1327, 1328, 1329, 1330, 1390, 1389, 1388, 1387, 1384, 1383, 1382, 1381, 1209, 1210, 1211, 1155, 1156, 1157, 1279, 1332, 1331, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1333, 1334, 1335, 1336, 1337, 1338, 1339, 1340, 1341, 1342, 1343, 1403, 1402, 1401, 1400, 1399, 1404, 1405, 1406, 1407, 1408, 1349, 1350, 1410, 1409, 1345, 1346, 1344, 1223, 1164, 1165, 1166, 1050, 1051, 1052, 977, 976, 975, 1347, 1348, 926, 925, 924, 861, 860, 859, 735, 734, 671, 670, 669, 668, 667, 666, 665, 664, 663, 662, 661, 601, 482, 483, 484, 485, 486, 487, 428, 429, 430, 431, 432, 427];
var values1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2];
var level4 = [1413, 400, 319, 0, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 780, 840, 900, 960, 720, 1020, 1080, 1140, 1200, 1260, 1320, 1380, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1483, 1494, 1495, 1496, 1497, 1498, 1499, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 16, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32, 25, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 48, 49, 50, 51, 47, 52, 53, 54, 55, 56, 57, 58, 59, 119, 179, 239, 299, 359, 419, 479, 599, 659, 539, 719, 779, 839, 899, 959, 1019, 1079, 1139, 1199, 1259, 1319, 1379, 1439, 241, 242, 243, 182, 307, 252, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 301, 302, 303, 376, 377, 316, 317, 378, 379, 380, 381, 382, 318, 320, 321, 322, 267, 268, 269, 383, 384, 385, 386, 387, 388, 389, 390, 391, 331, 332, 392, 333, 272, 273, 213, 214, 274, 334, 394, 454, 453, 393, 452, 451, 450, 449, 448, 447, 446, 445, 444, 443, 442, 441, 437, 436, 435, 434, 433, 432, 431, 430, 429, 428, 427, 426, 425, 423, 422, 421, 424, 438, 439, 440, 455, 456, 457, 458, 459, 460, 398, 461, 401, 341, 281, 282, 402, 342, 462, 463, 403, 343, 404, 464, 465, 466, 467, 468, 469, 470, 471, 407, 410, 472, 473, 1381, 1390, 1330, 1331, 1332, 1333, 1393, 1392, 1391, 1387, 1406, 1415, 1409, 1410, 1350, 1351, 1291, 1292, 1352, 1412, 1411, 1232, 1365, 1425, 1424, 1364, 1423, 1363];
var values4 = [5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2];
var level3 = [1187, 1185, 1069, 1063, 1239, 1440, 1380, 1320, 1260, 1200, 1140, 1080, 1020, 960, 900, 840, 780, 720, 660, 600, 540, 480, 420, 360, 300, 240, 180, 120, 60, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 119, 179, 239, 299, 359, 419, 479, 539, 599, 659, 719, 779, 839, 899, 959, 1019, 1079, 1139, 1199, 1259, 1319, 1379, 1439, 1499, 1498, 1497, 1496, 1495, 1494, 1493, 1492, 1491, 1490, 1489, 1488, 1487, 1486, 1485, 1484, 1483, 1482, 1481, 1480, 1479, 1478, 1477, 1476, 1475, 1474, 1473, 1472, 1471, 1470, 1469, 1468, 1467, 1466, 1465, 1464, 1463, 1462, 1461, 1460, 1459, 1458, 1457, 1456, 1455, 1454, 1453, 1452, 1451, 1450, 1449, 1448, 1447, 1446, 1445, 1444, 1443, 1441, 1442, 1384, 1385, 1325, 1265, 1266, 1326, 1386, 1270, 1271, 1334, 1335, 1336, 1337, 1274, 1277, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1338, 1339, 1399, 1400, 1340, 1341, 1401, 1402, 1342, 1343, 1403, 1404, 1344, 1345, 1405, 1406, 1346, 1347, 1407, 1408, 1348, 1349, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1378, 1377, 1376, 1375, 1374, 1373, 1372, 1371, 1370, 1369, 1368, 1367, 1366, 1365, 1364, 1363, 1362, 1361, 1360, 1359, 1358, 1357, 1356, 1355, 1354, 1353, 1352, 1351, 1350, 1333, 1332, 1331, 1330, 1329, 1328, 1327, 1279, 1280, 1281, 1224, 1167, 1110, 1053, 1297, 1296, 1298, 1299, 1300, 1301, 1302, 1064, 1068, 1123, 1183, 1243, 1303, 1129, 1189, 1249, 1309, 1308, 1307, 1306, 1305, 1304, 1244, 1184, 1248, 1188, 1247, 1246, 1245, 770, 830, 890, 950, 1010, 1070, 1130, 1190, 1250, 1310, 1242, 1182, 1122, 1062, 710, 1186, 1126, 1002, 1237, 1241, 1238, 1240, 1284, 1227, 1287, 1170, 1230, 1290, 1113, 1173, 1233, 1293, 650, 590, 589, 588, 587, 586, 585, 584, 583, 582, 642, 643, 644, 645, 646, 647, 648, 649];
var level5 = [1293, 1294, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 119, 179, 239, 299, 359, 419, 479, 539, 599, 659, 719, 779, 839, 899, 959, 1019, 1079, 1139, 1199, 1259, 1319, 1379, 1439, 1499, 1498, 1497, 1496, 1495, 1494, 1493, 1492, 1491, 1490, 1489, 1488, 1487, 1486, 1485, 1484, 1483, 1482, 1481, 1480, 1479, 1478, 1477, 1476, 1475, 1474, 1473, 1472, 1471, 1470, 1469, 1468, 1467, 1466, 1465, 1464, 1463, 1462, 1461, 1460, 1459, 1458, 1457, 1456, 1455, 1454, 1453, 1452, 1451, 1450, 1449, 1448, 1447, 1446, 1445, 1444, 1443, 1442, 1441, 1440, 1380, 1320, 1260, 1200, 1140, 1080, 1020, 960, 900, 840, 780, 720, 660, 600, 540, 480, 420, 360, 300, 240, 180, 120, 60, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 366, 365, 367, 184, 188, 489, 483, 542, 550, 129, 123, 307, 305, 494, 434, 374, 314, 254, 194, 134, 74, 675, 676, 677, 678, 679, 680, 681, 682, 495, 496, 497, 498, 499, 500, 501, 502, 442, 382, 322, 262, 202, 142, 82, 683, 684, 685, 686, 687, 688, 689, 85, 91, 558, 618, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 701, 700, 699, 698, 697, 696, 695, 694, 693, 692, 691, 690, 567, 568, 566, 452, 511, 512, 395, 396, 456, 455, 459, 581, 582, 642, 702, 762, 761, 760, 759, 758, 757, 756, 755, 754, 753, 752, 751, 750, 749, 748, 747, 746, 745, 744, 743, 742, 741, 740, 739, 738, 737, 736, 735, 734, 733, 732, 731, 730, 729, 728, 727, 726, 725, 724, 723, 722, 721, 643, 644, 645, 646, 647, 648, 708, 768, 767, 766, 765, 707, 706, 705, 704, 703, 763, 764, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1378, 1318, 1258, 1198, 1138, 1078, 1018, 958, 898, 838, 778, 718, 658, 598, 538, 478, 418, 358, 298, 238, 178, 118, 117, 116, 176, 177, 237, 236, 296, 297, 357, 356, 416, 417, 477, 476, 536, 537, 597, 596, 656, 657, 717, 716, 776, 777, 837, 836, 896, 897, 957, 956, 1016, 1017, 1076, 1077, 1137, 1136, 1196, 1197, 1257, 1256, 1316, 1317, 1377, 1376, 1242, 1241, 1296, 1295, 1051, 1050, 1167, 1164, 1101, 1217, 1213, 1212, 1211, 1210, 1209, 1273, 1333, 1393, 1392, 1391, 1390, 1389, 1388, 1328, 1268, 1208, 1272, 1332, 1331, 1330, 1329, 1269, 1270, 1271, 1207, 1267, 1327, 1387, 1150, 1206, 1205, 1204, 1203, 1202, 1201, 1261, 1321, 1381, 1382, 1383, 1384, 1385, 1386, 1326, 1266, 1265, 1264, 1263, 1262, 1322, 1323, 1324, 1325, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1375, 1365, 1364, 1363, 1366, 1362, 1361, 1360, 1359, 1358, 1357, 1356, 1355, 1354, 1353, 1352, 1351, 1350, 1349, 1348, 1347, 1346, 1345, 1344, 1343, 1342, 1341, 1340, 1339, 1338, 1337, 1336, 1335, 1334];
var values5 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 6, 6, 6, 6, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 7, 7, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2];
var values3 = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2];
var bCount = 0;
var bstate = [];
var values2 = [5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
var T_hath = [];
var level2 = [584, 949, 1306, 1298, 1227, 1397, 180, 182, 543, 544, 545, 1208, 1209, 1210, 240, 241, 242, 302, 362, 422, 482, 542, 602, 603, 604, 605, 665, 725, 785, 845, 905, 965, 1025, 1085, 1145, 1205, 1206, 1207, 1270, 1330, 1390, 1450, 1449, 1389, 1388, 1448, 1447, 1446, 1445, 1444, 1443, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900, 960, 1020, 1080, 1140, 1200, 1260, 1320, 1380, 1441, 1442, 1387, 1328, 1329, 1269, 1268, 1267, 1266, 1326, 1325, 1385, 1386, 1327, 1265, 1324, 1384, 1383, 1382, 1381, 1321, 1261, 1262, 1263, 1264, 1323, 1322, 1202, 1142, 1024, 1084, 1144, 1204, 1203, 1143, 1083, 1023, 1022, 1021, 1081, 1141, 1201, 1082, 962, 301, 361, 421, 481, 541, 601, 661, 721, 722, 662, 663, 723, 724, 664, 784, 783, 782, 781, 841, 842, 843, 844, 904, 903, 964, 963, 902, 901, 961, 1271, 1332, 1393, 1394, 1395, 1396, 1099, 1100, 1101, 1102, 991, 992, 993, 994, 995, 181, 125, 126, 127, 428, 429, 430, 1031, 1032, 1033, 1093, 1094, 1095, 1331, 1391, 1392, 1452, 1451, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1500, 1499, 1498, 1497, 583, 582, 581, 580, 643, 642, 641, 640, 644, 706, 344, 517, 516, 515, 392, 391, 267, 265, 266, 327, 326, 325, 324, 264, 263, 323, 390, 328];
var time_passed = 0;
var time_active = true;
var de_levels = [level1, values1, level2, values2, level3, values3, level4, values4, level5, values5];
var level_dat_u_on = 1;
var x = 100;
var y = 100;
var g = 0;
var gg = 0.4;
var grounded = false;
var colli = false;
var reloading = false;

function mouseClicked() {
	if (player_shooty_delay == 30 && ammo[0] > 0) {
		ammo[0]--;
		shotting(x + 10, y + 10, mouseX, mouseY, 'P')
		player_shooty_delay = 0
	} else if (ammo[0] == 0 && reloading == false) {
		reloading = true
		setTimeout(reload(), 1000)
	}
}

function reload() {
	if (ammo[1] > 0) {
		ammo[0] = 5;
		ammo[1]--;
	}
	reloading = false;
}

function shotting(xing, ying, xxing, yying, owner) {
	let i = 10;
	let angle1 = Math.atan2((xxing - (xing)), (yying - (ying)));
	let g = Math.sin(angle1) * i;
	let gg = Math.cos(angle1) * i;
	bull.push(xing);
	bull.push(ying);
	bull.push((xing) + g)
	bull.push((ying) + gg)
	bull.push(g)
	bull.push(gg)
	bull.push(owner)
}

function bullet_go_brr() {
	for (let a = 0; a < bull.length; a += 7) {
		bull[a] += bull[a + 4];
		bull[a + 1] += bull[a + 5]
		bull[a + 2] += bull[a + 4]
		bull[a + 3] += bull[a + 5]
		if (bull[a + 2] > windowWidth + 100 || bull[a + 2] < -100 || bull[a + 3] > windowHeight + 100 || bull[a + 3] < -100) {
			bull.splice(a, 7)
			continue;
		}
		strokeWeight(2);
		if (debug) {
			if (bull[a + 6] == 'E') {
				stroke(255, 0, 0)
			} else if (bull[a + 6] == 'P') {
				stroke(0, 0, 255)
			}
		}
		line(bull[a], bull[a + 1], bull[a + 2], bull[a + 3])
		strokeWeight(1);
		stroke(0)
	}
}

function gravity() {
	y += g;
	g += gg;
}

function draw() {
	if (time_go_slow >= wait || !debug) {
		time_go_slow = 0;
		T_dubug = []
		if (player_shooty_delay < 30) {
			player_shooty_delay++;
		}
		if (player_shooty_delay == 30 && ammo[0] > 0 && keys[32]) {
			ammo[0]--;
			shotting(x + 10, y + 10, mouseX, mouseY, 'P')
			player_shooty_delay = 0
		} else if (ammo[0] == 0 && reloading == false) {
			reloading = true
			setTimeout(reload(), 1000)
		}
		colli = false;
		override = false;
		background(255)
		cursor(CROSS)
		if (y < 500 - 20) {
			gravity();
			grounded = false;
		} else {
			while (y + 20 > 500) {
				y -= 0.4;
			}
			g = 0;
			grounded = true;
		}
		bcount = 0;
		tCount = 0;
		de_levels[level_dat_u_on - 1].forEach(load);
		player();
		bullet_go_brr();
		if (keys[82]) {
			death_counter--;
			let a = de_levels[level_dat_u_on].indexOf(3);
			death(spawn[0], spawn[1]);
		}
		fill(255, 255, 255, 100);
		rect(1100, 0, 100, 100);
		fill(0);
		textSize(15);
		text('Deaths:' + death_counter, 1110, 20);
		if (frameCount % 60 == 0 && time_active == true) {
			time_passed++;
		}
		let time_cal = Math.floor(time_passed / 60) + ':';
		if (time_passed % 60 < 10) {
			time_cal += '0' + time_passed % 60;
		} else {
			time_cal += time_passed % 60;
		}
		text('Time:' + time_passed, 1110, 40);
		text('Ammo:' + ammo[0] + '|' + ammo[1], 1110, 60);
		if (started == false) {
			started = true;
			let goofy = de_levels[level_dat_u_on - 1][de_levels[level_dat_u_on].indexOf(3)]
			death((goofy % 60) * 20, Math.floor(goofy / 60) * 20);
			T_hath = [];
			bstate = [];
			for (let abc in de_levels[level_dat_u_on]) {
				if (de_levels[level_dat_u_on][abc] == 6) {
					T_hath.push(4)
					delayyy.push(0);
				} else if (de_levels[level_dat_u_on][abc] == 7) {
					bstate.push(false)
				}

			}
		}
	}
	else {
		time_go_slow++;
	}

	if (keys[187]) {
		console.log('PlayerX:' + x + ' PlayerY:' + y + ' level on' + level_dat_u_on + ' ammo:' + ammo + ' hath:' + hath + ' deaths:' + death_counter)
		keys[187] = false
		debug = !debug;
	}
	if (debug) {
		fill(255)
		rect(1050, 0, 150, 220)
		textSize(13)
		fill(0)
		text('DEBUG INFO', 1050, 15)
		text('Player pos  X:' + Math.floor(x) + ' Y:' + Math.floor(y), 1050, 30)
		text('On Ground: ' + grounded, 1050, 45)
		text('bullets:' + bull, 1050, 60)
		text('started:' + started, 1050, 75)
		text('heath:' + hath, 1050, 90)
		text('time_active:' + time_active, 1050, 105)
		text('T heath' + T_hath, 1050, 120)
		text('Gravtiy:' + g, 1050, 135)
		text('colli:' + colli, 1050, 150)
		text('level:' + level_dat_u_on, 1050, 165)
		text('TSelect:' + TSelect, 1050, 180)
		text('slow time:' + wait + ' :' + time_go_slow, 1050, 195)
		text('Show Colisions:' + coliS, 1050, 210)
		if (keys[189]) {
			coliS = !coliS;
			keys[189] = false;
		}
		if (keys[39]) {
			wait++;
			keys[39] = false
		} else if (keys[37] && wait >= 0) {
			wait--;
			keys[37] = false
		}
		if (keys[38]) {
			keys[38] = false;
			TSelect++;
			if (TSelect > T_hath.length) {
				TSelect = 0;
			}
		} else if (keys[40]) {
			keys[40] = false;
			TSelect--;
			if (TSelect < 0) {
				TSelect = T_hath.length;
			}
		}
		for (var uwu in T_dubug) {
			if (de_levels[level_dat_u_on - 1].includes(T_dubug[uwu]) && de_levels[level_dat_u_on][de_levels[level_dat_u_on - 1].indexOf(T_dubug[uwu])] != 6) {
				fill(255, 0, 0)
				ellipse((T_dubug[uwu] % 60) * 20 + 10, Math.floor(T_dubug[uwu] / 60) * 20 + 10, 10, 10)
			} else {
				fill(0, 0, 255)
				ellipse((T_dubug[uwu] % 60) * 20 + 10, Math.floor(T_dubug[uwu] / 60) * 20 + 10, 10, 10)
			}
		}
	}
}

var xx = 0;
var yy = 0;
var asd = 0;
var dir = 1;
var spawn = [100, 100];
var override = false;
var radius = 8;
var angle123;
var delayyy = [];
var tCount = 0;
var random1 = [];
function bloopy_thing_ig(line1, line2, line3, line4) {
	let slope = (line4 - line2) / (line3 - line1);
	let inter = line2 - (line1 * slope);
	let hitMan = [];
	if (slope > 20 || slope == '-Infinity' || slope < -20) {
		for (let MA = Math.min(line2, line4); MA < Math.max(line2, line4); MA++) {
			let meep = (Math.floor(line1 / 20)) + (Math.floor(MA / 20) * 60);
			if (!hitMan.includes(meep)) {
				hitMan.push(meep)
			}
		}
	}
	for (let Moo = line1; Moo < Math.abs(line1 - line3) + line1; Moo++) {
		let cords_thingy;
		let XS;
		if (line1 > line3) {
			cords_thingy = ((line3 + (Moo - line1)) * slope) + inter;
			XS = Math.floor((line3 + (Moo - line1)) / 20)
		}
		else {
			cords_thingy = (Moo * slope) + inter;
			XS = Math.floor(Moo / 20)
		}
		let YS = Math.floor(cords_thingy / 20)
		fill(0, 255, 0)
		if (!hitMan.includes(XS + (YS * 60))) {
			hitMan.push(XS + (YS * 60))
		}
	}
	return hitMan;
}
function linRec(line1, line2, line3, line4, rec1, rec2, rec3, rec4) {
	let slope = (line4 - line2) / (line3 - line1);
	let inter = line2 - (line1 * slope)
	let range = [rec2 - (rec1 * slope), (rec2 + rec4) - ((rec1 + rec3) * slope), rec2 - ((rec1 + rec3) * slope), (rec2 + rec4) - (rec1 * slope)];
	if (inter >= range[0] && inter <= range[1] || inter >= range[2] && inter <= range[3]) {
		if (rec1 > Math.min(line1, line3) && rec1 < Math.max(line1, line3) || rec1 + rec3 > Math.min(line1, line3) && rec1 + rec3 < Math.max(line1, line3)) {
			if (rec2 > Math.min(line2, line4) && rec2 < Math.max(line2, line4) || rec2 + rec4 > Math.min(line2, line4) && rec2 + rec4 < Math.max(line2, line4)) {
				fill(255, 0, 0);
				return true;
			}
			else if (Math.min(line2, line4) > rec2 && Math.max(line2, line4) < rec2 + rec4) {
				fill(255, 0, 0);
				return true;
			}
			else {
				return false;
			}
		}
		else if (Math.min(line1, line3) > rec1 && Math.max(line1, line3) < rec1 + rec3) {
			if (rec2 > Math.min(line2, line4) && rec2 < Math.max(line2, line4) || rec2 + rec4 > Math.min(line2, line4) && rec2 + rec4 < Math.max(line2, line4)) {
				fill(255, 0, 0)
				return true;
			}
			else {
				return false;
			}
		}
		else {
			return false;
		}
	}
	if (line1 > rec1 && line1 < rec1 + rec3 && line2 > rec2 && line2 < rec2 + rec4 || line3 > rec1 && line3 < rec1 + rec3 && line4 > rec2 && line4 < rec2 + rec4) {
		fill(255, 0, 0)
		return true;
	}
}
function load(val, index) {
	colli = false;
	xx = 20 * (val % 60);
	yy = Math.floor(val / 60) * 20;
	switch (de_levels[level_dat_u_on][index]) {
		case 1://normal
			fill(100);
			break;
		case 2://death
			fill(245, 224, 80);
			break;
		case 3://spawn
			fill(220);
			break;
		case 4://goal
			fill(100, 130, 255);
			break;
		case 5://jump
			fill(255, 65, 105);
			break;
		case 6:
			fill(0, 0, 0)
			break;
		case 7:
			if (bstate[bcount] == false) {
				image(le_bullet_image, xx, yy);
			}
			break;
	}
	if (de_levels[level_dat_u_on][index] != 7) {
		rect(20 * (val % 60), Math.floor(val / 60) * 20, 20, 20);
	}

	if (de_levels[level_dat_u_on][index] == 5) {
		let jeffX = 20 * (val % 60);
		let jeffY = Math.floor(val / 60) * 20;
		fill(65, 105, 225);
		triangle(10 + jeffX, jeffY + 2, jeffX + 2, jeffY + 18, jeffX + 18, jeffY + 18);
	}
	else if (de_levels[level_dat_u_on][index] == 6 && T_hath[tCount] > 0) {
		let jeffX = 20 * (val % 60);
		let jeffY = Math.floor(val / 60) * 20;
		fill(0)
		rect(jeffX, jeffY, 20, 20)
		fill(200, 200, 0)
		for (let aca = 0; aca < 5; aca++) {
			noStroke();
			if (T_hath[tCount] >= aca) {
				fill(0, 255, 0);
			}
			else {
				fill(255, 0, 0);
			}
			rect(jeffX + aca * 4, jeffY - 10, 4, 4)
		}
		stroke(0)

		random1 = bloopy_thing_ig(jeffX + 10, jeffY + 10, x + 10, y + 10);//random1 is the all blocks between player
		let kirby = true;//says if found block
		if (TSelect == tCount && debug == true) {
			T_dubug = random1
		}
		for (var uwu in random1) {
			if (de_levels[level_dat_u_on - 1].includes(random1[uwu]) && de_levels[level_dat_u_on][de_levels[level_dat_u_on - 1].indexOf(random1[uwu])] != 6) {
				kirby = false;
				delayyy[tCount] = 0;
			}
		}
		if (kirby == true) {
			angle123 = Math.atan2(((y + 10) - (jeffY + 10)), ((x + 10) - (jeffX + 10)));
			if (asd < angle123) {
				asd += 0.03;
			}
			else if (asd > angle123) {
				asd -= 0.03;
			}
			if (asd > angle123 - 0.05 && asd < angle123 + 0.05) {
				asd = angle123;
			}
			if (asd > angle123 - 0.2 && asd < angle123 + 0.2) {
				if (delayyy[tCount] < 20) {
					delayyy[tCount]++;
				}
				else {
					let XXXX = Math.cos(asd) * radius + jeffX + 10;
					let YYYY = Math.sin(asd) * radius + jeffY + 10;
					strokeWeight(10);
					shotting(XXXX, YYYY, x + 10, y + 10, 'E');
					strokeWeight(1);
					delayyy[tCount] -= 10;
				}
			}
			else {
				delayyy[tCount] = 0;
			}
		}
		let XXX = Math.cos(asd) * radius + jeffX + 10;
		let YYY = Math.sin(asd) * radius + jeffY + 10;
		stroke(0, 255, 0);
		ellipse(XXX, YYY, 5, 5);
		stroke(0);
	}
	if (de_levels[level_dat_u_on][index] == 6) {
		tCount++;
	}
	for (let bloop = 0; bloop < bull.length; bloop += 7) {
		if (bull[bloop + 6] == "E" && de_levels[level_dat_u_on][index] == 6) {
			continue;
		}
		var bonk = false;
		bonk = linRec(bull[bloop], bull[bloop + 1], bull[bloop + 2], bull[bloop + 3], xx, yy, 20, 20);
		if (bonk == true && bull[bloop + 6] == 'P' && de_levels[level_dat_u_on][index] == 6 && T_hath[tCount - 1] > 0) {
			T_hath[tCount - 1]--;//why is it shooting its self????
		}
		if (bonk == true) {
			if (de_levels[level_dat_u_on][index] == 7 && bstate[bcount] == false || de_levels[level_dat_u_on][index] != 7) {
				bull.splice(bloop, 7);
			}
		}
	}
	if (g < 0) { dir = 1; } else { dir = -1; }
	if ((x > xx - 20 && x < xx + 20 && y > yy - 20 && y < yy + 20)) { colli = true }
	while ((x > xx - 20 && x < xx + 20 && y > yy - 20 && y < yy + 20) && override == false) {
		if (de_levels[level_dat_u_on][index] != 7) {
			g = 0;
			y += dir / 5;
			grounded = true;
		}
		else {
			break;
		}
	}
	if (colli == true) {
		collision(xx, yy, de_levels[level_dat_u_on][index]);
	}
	if (de_levels[level_dat_u_on][index] == 3) {
		spawn[0] = xx;
		spawn[1] = yy;
	}
	if (de_levels[level_dat_u_on][index] == 7) {
		bcount++;
	}
}
function collision(x, y, value) {
	if (coliS) {
		fill(0, 255, 0, 200)
		rect(xx, yy, 20, 20)
	}
	switch (value) {
		case 2:
			death(spawn[0], spawn[1]);
			break;
		case 4:
			if (level_dat_u_on + 2 < de_levels.length) {
				level_dat_u_on += 2;
				started = false;
				death_counter--;
			}
			else {
				console.error('404 next level not found');
				time_active = false;
			}
			break;
		case 5:
			g = -10;
			y -= 0;
			grounded = false;
			override = true;
			break;
		case 7:
			if (bstate[bcount] == false) {
				ammo[1]++
			}
			bstate[bcount] = true
			break;
	}
}

function player() {
	bcount = 0;
	if (keys[68]) {
		x += movement_speed;
		for (i = 0; i < de_levels[level_dat_u_on - 1].length; i++) {
			xx = 20 * (de_levels[level_dat_u_on - 1][i] % 60);
			yy = Math.floor(de_levels[level_dat_u_on - 1][i] / 60) * 20;
			if ((x > xx - 20 && x < xx + 20 && y > yy - 20 && y < yy + 20) && de_levels[level_dat_u_on][i] != 5) {
				collision(xx, yy, de_levels[level_dat_u_on][i]);
			}
			while ((x > xx - 20 && x < xx + 20 && y > yy - 20 && y < yy + 20)) {
				if (de_levels[level_dat_u_on][i] != 7) {
					x -= 0.4;
				}
				else {
					break;
				}
			}
		}
	}
	if (keys[65]) {
		x -= movement_speed;
		for (i = 0; i < de_levels[level_dat_u_on - 1].length; i++) {
			xx = 20 * (de_levels[level_dat_u_on - 1][i] % 60);
			yy = Math.floor(de_levels[level_dat_u_on - 1][i] / 60) * 20;
			if ((x > xx - 20 && x < xx + 20 && y > yy - 20 && y < yy + 20) && de_levels[level_dat_u_on][i] != 5) {
				collision(xx, yy, de_levels[level_dat_u_on][i]);
			}
			while ((x > xx - 20 && x < xx + 20 && y > yy - 20 && y < yy + 20)) {
				if (de_levels[level_dat_u_on][i] != 7) {
					x += 0.4;
				}
				else {
					break;
				}
			}
		}
		if (de_levels[level_dat_u_on][i] == 7) {
			bcount++;
		}
	}
	if (keys[87] && grounded == true) {
		y -= 2;
		g = -jumpH;
		keys[87] = false;
	}
	fill(255, 0, 0);
	for (let MMM = 0; MMM < 5; MMM++) {
		noStroke();
		if (hath >= MMM) { fill(0, 200, 0) }
		else { fill(255, 0, 0) }
		rect(x + MMM * 4, y - 10, 4, 4)
	}
	stroke(0);
	if (hath < 0) {
		death(spawn[0], spawn[1])
	}
	for (let bloop = 0; bloop < bull.length; bloop += 7) {
		let qwer = linRec(bull[bloop], bull[bloop + 1], bull[bloop + 2], bull[bloop + 3], x, y, 20, 20)
		if (qwer == true && bull[bloop + 6] == "E") {
			bull.splice(bloop, 7)
			hath--;
		}

	}
	fill(255, 0, 0);
	rect(x, y, 20, 20);
}
function death(spawnX, spawnY) {
	g = 0;
	hath = 5;
	x = spawnX;
	y = spawnY - 30;
	death_counter++;
}
