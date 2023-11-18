Travail demandé
Interface graphique 2D interactive (en Python ou Matlab ou C++) permettant de
– la lecture d’un fichier contenant une polyligne fermée d’une forme 2D
– dessiner un contour à la souris (polylignes, plusieurs courbes de Bézier,...)
– sélectionner un point du maillage et le déplacer (pour la manipulation de la forme).
Maillage: calculer un maillage 2D du contour de la forme. Il s’agit de calculer une "tri- angulation contrainte". Le nombre de sommets de votre polyligne détermine la resolution du maillage. Choisir une structure de données adaptée. Certains librairies (Triangle de Shewchuk, CGAL) ou programmes (Matlab, Python) proposent cette méthode.
Définir les handles et sommets fixes, dans votre interface graphique interactive.
Calculer la déformation : Pour simplifier le travail, on peut d’abord implémenter une simple déformation Laplacien en suivant le premier paragraphe 4.1 du papier et en se reférant au papier [Sorkine 2004]. Quand la déformation Laplacien de base fonctionne, on cherchera à améliorer avec des méthodes plus compliquées décrites dans le papier.
Si vous trouvez des codes déjà existants pour les étapes décrites ci-dessus, vous pouvez les utiliser en le citant clairement dans votre rapport.