# Making Classes
In this section, we will discuss making and then using classes

## What are Classes?
Classes are templates after which you can create objects. 

Example an Object Person 

The person might have the following attributes.

- Name
- Birthday
- Hair color
- Gender
- 2 Parents (which are also persons)

Now we can create a person after precisely this scheme.

- Peter Example
- 12.3.2001
- Black
- Male
- Max and Joseph

Using this scheme, we can create a list of objects with different attributes much more straightforward than by having a variable for each one of them.

### Functions in Classes
Classes can not only hold variables - but they can also have functions

``` python
    class example():
        def helloWorld(self):
            print('Hello World')
```
This would print 
```
Hello World
```


## Your task
Create a class person which contains these Parameters
- Name
- Birthday (Should be a String)
- Hair color *(Referenced as hair)*
- Gender

 It should also have a function changeName(newName) which changes the name of the Person.

As well as a Function which changes the Hair color of the Person, with the name changeHairColor(newHairColor)

