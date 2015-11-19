use re7;

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
INSERT INTO Ingredient VALUES (1,'lait'),(2,'huile'),(3,'sel'),(4,'farine');
UNLOCK TABLES;
