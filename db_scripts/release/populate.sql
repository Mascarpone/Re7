LOCK TABLES `Category` WRITE;
INSERT INTO `Category` VALUES (1,'entrée'),(2,'plat'),(3,'dessert');
UNLOCK TABLES;

LOCK TABLES `Ingredient` WRITE;
INSERT INTO `Ingredient` VALUES (1,'lait',2),(2,'huile',5),(3,'sel',6),(4,'farine',1);
UNLOCK TABLES;

LOCK TABLES `Recipe` WRITE;
INSERT INTO `Recipe` VALUES (1,'Ptit dej\'',4,1,5,0,1,1),(2,'Jambon coquillettes',3,1,5,10,1,2),(3,'Steack haché frites',5,1,5,15,1,3),(4,'Test',10,2,12,12,1,1);
UNLOCK TABLES;

LOCK TABLES `Unit` WRITE;
INSERT INTO `Unit` VALUES (1,'g'),(2,'cl'),(3,'l'),(4,'cuillère(s) à soupe'),(5,'cuillère(s) à café'),(6,'pincée(s)');
UNLOCK TABLES;

LOCK TABLES `User` WRITE;
INSERT INTO `User` VALUES (1,'admin','root');
UNLOCK TABLES;

