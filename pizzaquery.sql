select Person.name, Person.age, Person.gender
From Person
Where Person.gender= 'male' AND Person.age > 18;

Select Person.name, Person.age, Person.gender
From Person
Where Person.gender = 'female' AND Person.age >= 30;

Select p.name
From Person p Inner Join Eats e ON p.name = e.name
Where p.gender = 'male' AND e.pizza = 'cheese';

Select Distinct Pizzeria
From Serves
Where Pizzeria Not In(Select pizzeria From Serves Where price>=9);

Select Distinct Pizzeria
From Serves
Where Pizzeria Not In (Select Pizzeria From Serves Where price <9);

Select Distinct e.pizza
From Person p
Join Eats e ON p.name = e.name
Join Serves s ON e.pizza = s.pizza
Where p.gender = 'female' AND p.age > 20 AND s.price > 9;


Select Distinct e.Pizza
From Eats e, Serves s, Frequents f
Where e.name = f.name AND e.pizza = s.pizza AND f.pizzeria = s.pizzeria AND price >9 AND f.name IN (Select name From Person Where age >20 AND gender = 'female');

Select Distinct e.name
From Eats e
Join Serves s ON e.pizza = s.pizza
Where s.pizzeria = 'Dominos' AND e.name Not In(Select f.name From Frequents f Where f.pizzeria = 'Dominos');


Select Distinct e.pizza
From Eats e
Where e.name In (Select p.name From Person p Where p.age <24) 
AND e.name Not In(Select p.name From Person p Where p.age >=24);



