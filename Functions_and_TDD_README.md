# Functions and TDD Documentation

## TDD

### User story ML:
    As a <user>
    I want to <do_something>
    
### Product backlog
### Sprint Backlog
### Doing
### Done

## Sprint Artifacts as 'radiators'
- sends 'heat' - artifacts can relate to other parts of a project's DOD
- DOD - definition of done - defines criteria for user stories that are common to all user stories
- Acceptance criteria: user stories have at least 2 tests in this
- All tests are passed - acceptance criteria fulfilled

- Where appropriate, acceptance criteria should have documentation
- should follow Python conventions
- A project should be in its own repository branch if successfully merged on origin

- Definition of scrum framework NOT CARDS

EPIC vs user story: "As a user, I want to be able to <overall project aim>"

### Project/Sprint planning
- Prioritisation and estimation of effort
- Estimation largely relies on collective knowledge and team experience
- Prioritisation is largely based on what the product owner wants vs what is realistic and provides the most value
- in the context of the bread factory project, if a user wants to make wholemeal and not white bread
  as a way to efficiently use factory downtime to test niche markets
  

### TDD & testing
- Testing individual blocks of code to verify functionality

pros:
- avoids technical debt
- know your code is working 
- Understanding of your code improves
- more re-usable/scalable code
- easier to debug
- easier to maintain
- reduce costs
- reduce spaghetti code (unreadable or hard to understand code)
- attract better talent for projects

cons:
- you have to write the tests
- bad tests will result in bad code

### Unit Testing

- tests a single part of code or function
- relates to user stories

### Integration testing

- tests the entire program or system as a whole

## Functions

- functions are like people at work: one job
- easier to test functions doing only one job

#### how do functions work? 

##### Define a method ML:
        def example_function(param):
        return something
        
- define and call a method to run blocks of code
- whereas variables are containers, functions are "cookers"
- they can take in arguments or parameters (but are not required to)
- they are dynamic and can morph the output
####      ML:
         mr_miyagi_question = input()
         functional_miyagi(mr_miyagi_question)
         
- A function is like a machine
- It can interact with things, take input and follow a set of instructions

- Why functions - reusable code (DRY)

#### Best practices for functions
- Naming conventions, lower case, python_case
- Call with () e.g my_function()

##### Separation of concerns

- exists at network, infrastructure and code level
- design separate from procedure, procedure separate from distribution, distribution separate from consumer
- opens and prevents a single point of failure
- makes code more maintainable


DO NOT PRINT IN FUNCTIONS (ONLY TO DEBUG)

- Basis of a test: has known or controlled inputs and expected outputs
- Assertions: to assert if input results in expected output (True/False)
#### ML:
        known_input_1 = <name>
        expected_output = <result>
        
- When importing from other files, best to import specific function


 
   


