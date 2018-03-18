from Classes import *
import sys

TheNationals = Team("Washington Nationals")


p1 = Player('Bryce Harper', TheNationals, 'LF', 413, range(611, 995), range(335, 468), range(468, 473,), range(473, 611), range(1, 335), range(995, 1001), range(1, 348),  range (402, 1001), range (348, 402))
p2 = Player('Matt Weiters', TheNationals,'TBC', 288, range(507, 993), range(284, 433), range(1002,1003), range(433, 507), range(1, 284), range(993, 1001), range(716, 1001), range(42, 716), range(1, 42))
p3 = Player('Ryan Zimmerman', TheNationals, '1B', 358, range(549, 985), range(214, 374), range(1002,1003), range(374, 549), range(1, 214), range(985, 1001), range(659, 1001), range(43, 659), range(1, 43))
p4 = Player('Daniel Murphy', TheNationals, 'TBC', 384, range(531, 982), range(228, 417), range(417, 430), range(430, 531), range(1, 228), range(982, 1001),range(789, 1001), range(44, 789), range(1, 44))
p5 = Player('Trea Turner', TheNationals, 'TBC', 338, range(470, 974), range(199, 358), range(358, 397), range(397, 470), range(1, 199), range(974, 1001), range(730, 1001), range(14, 730), range(1, 14))
p6 = Player('Anthony Rendon', TheNationals, 'TBC', 403, range(619, 971), range(344, 512), range(512, 516), range(516, 619), range(1, 244), range(971, 1001), range(773, 1001), range(19, 773), range(1, 19))
p7 = Player('Jason Werth', TheNationals, 'TBC', 322, range(602, 989), range(376, 484), range(484, 495), range (495, 602), range(1, 93), range(989, 1001), range(648, 1001), range(20, 648), range(1, 20))
p8 = Player('Michael Taylor', TheNationals, 'TBC,', 320, range(536, 993), range(210, 377), range(377, 399), range(399, 536), range(1, 210), range(993, 1001), range(534, 1001), range(10, 534), range(1, 10))
p9 = Player('Wilmer Difo', TheNationals, 'TBC', 319, range(374, 991), range(209, 296), range(296, 330), range(330, 374), range(1, 209), range(991, 1001), range(704, 1001), range(28, 704), range(1, 28))
p10 = Player('Adam Lind', TheNationals, 'TBC', 362, range(514, 1001), range(257, 385), range(1002, 1003), range(385, 514), range(1, 257), range(1003, 1004), range(755, 1001), range(31, 755), range(1, 31))

TheNationals.Players = [p1,
						p2,
						p3,
						p4,
						p5,
						p6,
						p7,
						p8,
						p9]


TheMets = Team("New York Mets")

p11 = Player("Travis d'Arnoud", TheMets, 'TBC', 293, range(536, 982), range(209, 382), range(382, 391), range(391, 536), range(1, 209), range(982, 1001), range(778, 1001), range(45, 778), range(1, 45))
p12 = Player('Lucas Duda', TheMets, 'TBC', 347, range(743, 980), range(366, 574), range(1002, 1003), range(574, 743), range(1, 366), range(980, 1001), range(616, 1000), range(32, 616), range(1, 32))
p13 = Player('Neil Walker', TheMets, 'TBC', 339, range(515, 960), range(267, 396), range(396, 416), range(416, 515), range(1, 267), range(960, 1001), range(763, 1001), range(20, 763), range(1, 20))
p14 = Player('Jose Reyes', TheMets, 'TBC', 315, range(554, 989), range(286, 429), range(429, 469), range(469, 554), range(1, 286), range(989, 1001), range(795, 1001), range(8, 795), range(1, 8))
p15 = Player('Wilmer Flores', TheMets, 'TBC', 307, range(477, 973), range(153, 306), range(306, 315), range(315, 477), range(1, 153), range(973, 1001), range(785, 1001), range(56, 785), range(1, 56))
p16 = Player('Yoenis Cespedes', TheMets, 'TBC', 352, range(549, 982), range(230, 381), range(381, 398), range(398, 549), range(1, 230), range(982, 1001), range(707, 1001), range(34, 707), range(1, 34))
p17 = Player('Juan Lagares', TheMets, 'TBC', 296, range(438, 963), range(175, 375), range(375, 400), range(400, 438), range(1, 175), range(963, 1001), range(708, 1001), range(31, 708), range(1, 31))
p18 = Player('Jay Bruce', TheMets, 'TBC', 321, range(611, 993), range(271, 410), range(1004, 1005), range(410, 611), range(1, 271), range(993, 1001), range(664, 1001), range(30, 664), range(1, 30))
p19 = Player('Asdrubal Carbrera', TheMets, 'TBC', 351, range(508, 974), range(265, 434), range(1004, 1005), range(434, 508), range(1, 265), range(974, 1001), range(764, 1001), range(54, 764), range(1, 54))
p20 = Player('Michael Conforto', TheMets, 'TBC', 384, range(621, 953), range(337, 456), range(456, 462), range(462, 621), range(1, 337), range(953, 1001), range(583, 1001), range(11, 583), range(1, 11))



TheMets.Players = [p11,
					p12,
					p13,
					p14,
					p15,
					p16,
					p17,
					p18,
					p19,
					p20]

b1 = Base('The Plate')
b2 = Base('Base 1')
b3 = Base('Base 2')
b4 = Base('Base 3')

Bases = [b1,b2,b3,b4]

TheGame = Game(TheNationals, TheMets)
TheGame.PlayBall(Bases)
print(sys.path[0])
