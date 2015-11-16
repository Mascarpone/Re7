LOCK TABLES Category WRITE;
INSERT INTO Category VALUES (1,'Apéritif'),(2,'Entrée'),(3,'Plat'),(4,'Dessert');
UNLOCK TABLES;

LOCK TABLES User WRITE;
INSERT INTO User VALUES (1,'admin','root');
UNLOCK TABLES;

LOCK TABLES Unit WRITE;
INSERT INTO Unit VALUES (1,'(Rien)'),(2,'grammes (gr)'),(3,'kilogrammes (kg)'),(4,'litres (l)'),(5,'millilitres (ml)'),(6,'centilitres (cl)'),(7,'c. à café'),(8,'c. à soupe'),(9,'c. à thé');
UNLOCK TABLES;

LOCK TABLES Ingredient WRITE;
INSERT INTO Ingredient VALUES (1,'lait',4),(2,'huile',5),(3,'sel',6),(4,'farine',1);
UNLOCK TABLES;

LOCK TABLES Recipe WRITE;
INSERT INTO Recipe VALUES (1,'Ptit dej\'',4,1,5,0,1,1),(2,'Jambon coquillettes',3,1,5,10,1,2),(3,'Steack haché frites',5,1,5,15,1,3),(4,'Test',10,2,12,12,1,1);
UNLOCK TABLES;
