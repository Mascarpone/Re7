use re7;

INSERT INTO Category VALUES (1,'Apéritif'),(2,'Entrée'),(3,'Plat'),(4,'Dessert'),(5,'Viande'),(6,'Poisson'),(7,'Légume'),(8,'Fruit'),(9,'Fromage');

INSERT INTO User VALUES (1,'admin','root'),(2,'scassiau','okok'), (3,'gbea','okok'),(4,'flevern','okok'),(5,'test','test');

INSERT INTO Unit VALUES (1,'(Rien)'),(2,'grammes'),(3,'kilogrammes'),(4,'litres'),(5,'millilitres'),(6,'centilitres'),(7,'c. à café'),(8,'c. à soupe'),(9,'pincée');

INSERT INTO Ingredient VALUES (1,'Lait'),(2,'Huile'),(3,'Sel'),(4,'Farine'),(5,'Chocolat noir'),(6,'Poivre'),(7,'Crème'),(8,'Oeuf(s)'),(9,'Beurre'),(10,'Blanc(s) de poulet'),(11,'Oignon'),(12,'Curry');

INSERT INTO Recipe VALUES
(1, "Poulet au Curry", "pouletcurry.jpg", 8.50, 2, 3, 10, 4, 5);

INSERT INTO Step VALUES
(1, "Coupez les blancs de poulet en petits morceaux ainsi que l'oignon.", 1),
(2, "Faite revenir l'oignon dans une poele à feu moyen.", 1),
(3, "Rajoutez les blancs de poulet dans la poele. Salez, poivrez.", 1),
(4, "Lorsque c'est cuit, ajouter le curry et la crème fraiche.", 1),
(5, "A déguster chaud accompagné de riz ou de pommes de terre sautées.", 1);

INSERT INTO Contain VALUES
(1, 7, 2, 1, 8),
(1, 10, 1, 1, 1),
(1, 11, 0.25, 0, 1),
(1, 12, 1, 1, 9);

INSERT INTO Comment VALUES
(1, "C'est délicieux je vous le recommande j'en fais très souvent !", 5, 4, 5, CURRENT_TIMESTAMP, 5, 1);
