use re7;

INSERT INTO Category VALUES (1,'Apéritif'),(2,'Entrée'),(3,'Plat'),(4,'Dessert'),(5,'Viande'),(6,'Poisson');

INSERT INTO User VALUES (1,'admin','root'),(2,'scassiau','okok'), (3,'gbea','okok'),(4,'flevern','okok'),(5,'test','test');

INSERT INTO Unit VALUES (1,'(Rien)'),(2,'grammes'),(3,'kilogrammes'),(4,'litres'),(5,'millilitres'),(6,'centilitres'),(7,'c. à café'),(8,'c. à soupe'),(9,'pincée');

INSERT INTO Ingredient VALUES (1,'Lait'),(2,'Huile'),(3,'Sel'),(4,'Farine'),(5,'Chocolat noir'),(6,'Poivre'),(7,'Crème'),(8,'Oeuf(s)'),(9,'Beurre'),(10,'Blanc(s) de poulet'),
                              (11,'Oignon'),(12,'Curry'),(13,'Lardons'),(14,'Reblochon'),(15,'Pomme(s) de terre'),(16,'Champagne'),(17,'Sucre de canne'),(18,'Framboise(s)'),(19,'Grand Marnier'),(20,'Riz'),
                              (21,'Vinaigre'),(22,'Saumon'),(23,'Avocat'),(24,'Concombre'),(25,'Sucre'),(26,'Mascarpone'),(27,'Café'),(28,'Biscuit(s) cuillère'),(29,'Cacao');

INSERT INTO Recipe VALUES
(1, "Poulet au Curry", "pouletcurry.jpg", 8.50, 2, 3, 10, 4, 5),
(2, "Tartiflette classique", "tartiflette.jpg", 10, 2, 15, 15, 4, 3),
(3, "Soupe de champagne aux framboises", "champagne.jpg", 16, 1, 5, 0, 4, 1),
(4, "Makis simples", "makis.jpg", 5, 3, 20, 15, 4, 6),
(5, "Tiramisu maison", "tiramisu.jpg", 4.50, 4, 20, 0, 4, 4);

INSERT INTO Step VALUES
(1, "Coupez les blancs de poulet en petits morceaux ainsi que l'oignon.", 1),
(2, "Faite revenir l'oignon dans une poele à feu moyen.", 1),
(3, "Rajoutez les blancs de poulet dans la poele. Salez, poivrez.", 1),
(4, "Lorsque c'est cuit, ajouter le curry et la crème fraiche.", 1),
(5, "A déguster chaud accompagné de riz ou de pommes de terre sautées.", 1),
(1, "Faites cuire les pommes de terre.", 2),
(2, "Faites chauffer dans une petite casserolle les lardons, l'oignon découpé et la crème (ne pas mettre de sel !).", 2),
(3, "Découper les pommes de terre en lamelles et disposer les dans votre récipient. Verser dessus la préparation précédente et recouvrez du demi reblochon coupé selon la tranche.", 2),
(4, "Enfourner à 200°C jusqu'à ce que le fromage soit doré (environ 15 min).", 2),
(1, "Mettre les framboises dans le mélange Grand Marnier-Sucre de canne et laisser mariner au réfrigérateur toute une nuit.", 3),
(2, "Au moment de servir, mettre un fond de cette préparation dans la flûte et rajouter le champagne.", 3),
(1, "Lavez le riz (riz rond de préférence) et faites le cuire.", 4),
(2, "Ajouter le vinaigre spécial sushi au riz (goutez jusqu'à satisfaction) et laissez refroidir.", 4),
(3, "Coupez les ingrédients de la garniture en lamelles.", 4),
(4, "Roulez les makis en étalant du riz sur une feuille d'algue, et en ayant disposé les lamelles de garnitures le long d'un des cotés. Découpez selon la taille voulue.", 4),
(5, "Astuce : pour éviter que le riz ne colle trop aux doigts, se les rincer dans de l'eau salée. Ajoutez de l'extrait de café (si vous avez) au café froid.", 4),
(1, "Préparez du café noir. Séparez les blancs des jaunes. Mélangez les jaunes, le sucre puis le mascarpone avec un fouet dans un grand saladier. Puis réserver au réfrigirateur.", 5),
(2, "Montez les blancs en neige fermes et les incorporer délicatement à la spatule au mélange précédent.", 5),
(3, "Mouillez la moitié basse des biscuits et les déposer dans le plat.", 5),
(4, "Recouvrez d'une couche de la préparation et saupoudrez de cacao. Recommencez à l'étape 3 jusqu'à épuisement des ressources en finissant par une couche de crème.", 5),
(5, "Mettre au réfrigirateur au moins 4 heures et ne saupoudrez le tout de cacao qu'avant de servir.", 5);

INSERT INTO Contain VALUES
(1, 7, 2, 1, 8),
(1, 10, 1, 1, 1),
(1, 11, 0.25, 0, 1),
(1, 12, 1, 1, 9),
(2, 13, 50, 0, 2),
(2, 15, 10, 1, 1),
(2, 14, 1, 1, 1),
(2, 11, 0.25, 0, 1),
(2, 7, 2, 1, 8),
(3, 16, 1, 1, 1),
(3, 17, 200, 0, 5),
(3, 19, 200, 0, 5),
(3, 18, 300, 1, 2),
(4, 20, 100, 1, 2),
(4, 22, 50, 1, 2),
(4, 23, 1, 0, 1),
(4, 24, 0.5, 0, 1),
(4, 21, 3, 0, 8),
(5, 8, 3, 0, 1),
(5, 26, 250, 1, 2),
(5, 28, 15, 1, 1),
(5, 25, 100, 0, 2),
(5, 27, 30, 1, 6),
(5, 29, 30, 1, 2);

INSERT INTO Comment VALUES
(1, "C'est délicieux je vous le recommande j'en fais très souvent !", 5, 4, 5, CURRENT_TIMESTAMP, 5, 1),
(2, "Parfait pour les soirs d'hiver.", 5, 5, 5, CURRENT_TIMESTAMP, 4, 2),
(3, "Ma grand-mère s'est saoulée avec ca à mes 20 ans ... un régal !", 4, 3, 5, CURRENT_TIMESTAMP, 4, 3),
(4, "Oishii desu ne !", 5, 3, 3, CURRENT_TIMESTAMP, 5, 4);
