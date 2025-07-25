
# HBnB Project

## Introduction
The HBNB project is a mini-version of the Airbnb website.
The user can set some informations about the place, users, review and amenity.
This document constitutes the complete technical information for this project.
It brings together all the UML diagrams produced to illustrate the application architecture, the business logic and the communication flows between layers. 
The goal is to provide a clear, readable and structured explanation of our project.



## Package Diagram 
In this diagramm, the purpose is to show how the global architecture of the application work. It illustrates how to application is modularly divided into three keys logical layers. 
This diagram helps developers quickly understand the structure and responsibility of each major part of the application without diving into the implementation details.

```mermaid
graph TD
    subgraph UI [User Interface]
        A[Services API]
    end
    subgraph BL [Business Logic]
        B[ModelClasses]
    end
    subgraph DB [Database]
        C[DatabaseAccess]
    end
    
    A --> B
    B --> C
```

🔹Key components

1️⃣ UserInterface

Contains Services and API components.

Handles external user interactions, such as HTTP requests.

2️⃣ BusinessLogic

Contains core ModelClasses such as User, Place, Review, and Amenity.

Implements the application's rules and workflows.

3️⃣ DataBase

Contains DataBaseAccess components, typically involving repositories or data mappers.

Responsible for storing and retrieving persistent data.

↪️ Communication Arrows

UserInterface --> BusinessLogic is done via a Facade to decouple the frontend logic from core rules.

BusinessLogic --> DataBase represents Database Operations.

    
## Class Diagram 

* This diagram discribe the business logic layer and interaction with the different Logic component.
  
* This diagram represent 4 Class :
  - Place where the user can live for a night or more
  - The amenity of the place Wifi, Number of pieces, Number of piece
  - The user connect to the website and if the user is an admin with more power of moderate the website
  - The review with the notation of a place by a user and comments about the place
  - AMENITY, USER, PLACE AND REVIEW are the entity use by the website via the BusinessLogicLayer

* Each class have field like date creation, date modification and a uniq id needed by the Database to identify the place, the review, the amenity or the user.

* This class diagram provide data and function usefull for the interaction between the facade patern and the database
* You can create, update, delete a REVIEW
* You can create, update, delete a PLACE
* You can create, update, delete a AMENITY
* You can create, update, delete a USER

* Interaction between class : 
  - First the place have some amenity, a amenity cannot exist without place. 
  - A place is located by a user, this user can make a review about the quality of service. 
  - Relation between place and review : 
  - 1 place can have many review
  - 1 Review is written by one user and one place
  - 1 user can create many review

```mermaid
classDiagram
direction TB
namespace BusinessLogicLayer {


    class AmenityEntity {
+int idAmenity
    +String name
    +String description
    +int idPlace
    +Date dateCreation
    +Date dateModification
    +createAmenity()
    +updateAmenity()
    +deleteAmenity()
    }

    class ReviewEntity {
    +Float rating
    +String comment
    +Date dateCreation
    +Date dateModification
    +int idPlace
    +int idUser
    +listReviewByPlace(idPlace) List Review
    +listReviewByUser(idUser) List Review
+createReview()
    +updateReview()
    +deleteReview()
    }

    class UserEntity {
    +int idUser
    +String firstName
    +String lastName
    +String email
    +String password
    +bool isAdmin
    +Date dateCreation
    +Date dateModification
    +isAdmin()
    +createUser()
    +updateUser()
    +deleteUser()
+listUser()
+listAdmin()
    }

    class PlaceEntity {
    +int idPlace
    +String title
    +String description
    +Float price
    +Float latitude
    +Float longitude
    +Date dateCreation
    +Date dateModification
    +createPlace()
    +updatePlace()
    +deletePlace()
+listPlace()
+listAmenity(idPlace) List:Amenity
    }
}
    PlaceEntity *-- AmenityEntity
    PlaceEntity "1" -- "*" ReviewEntity
    ReviewEntity "*" -- "1" UserEntity
```

## Sequence Diagram
In this Sequence we created sequence diagrams that represent the flow of interactions across the different layers of the application for specific API calls. These diagrams show how the presentation layer, business logic and persistence layer communicate with each other to handle user requests. 

## User Registration
User account creation process. The user fills in their information on the homepage, which is transmitted via the web API to be stored in the database with confirmation email sending.
```mermaid
sequenceDiagram
    participant User
    participant Homepage
    participant "Web API" as API
    participant Database
    
    User->>Homepage: CreateNewAccount
    User->>Homepage: EnterUserDetails
    User->>Homepage: ClickSubmit
    Homepage->>API: CreateNewAccount
    API->>Database: RegisterUserDetails
    Database-->>API: SaveUser
    API-->>Homepage: SendEmailConfirmation
```
Key Interactions:

- Form validation occurs both client-side and server-side
- Password encryption is handled by the API layer
- Email confirmation ensures user authenticity
- Database transactions ensure data consistency

## Place creation
Simplified listing creation process. The user enters their listing details on the website, which saves them directly to the database and confirms successful creation.

```mermaid
sequenceDiagram
    participant User
    participant Website
    participant Database
    
    User->>Website: Fill in listing details
    Website->>Database: Save listing details
    Database-->>Website: Confirmation of saving
    Website-->>User: Listing successfully created
```
Key Interactions:

- User input validation occurs at the website level
- Business logic handles search algorithm implementation
- Database queries are optimized for performance
- Results are cached for subsequent similar requests

## Review Submission
User review submission flow. The system processes and validates the review through business logic before storing it in the database and confirming submission to the user.

```mermaid
sequenceDiagram
    participant User
    participant Website
    participant BusinessLogic
    participant Database
    
    User->>Website: Submit review
    Website->>BusinessLogic: Process review
    BusinessLogic->>Database: Validate and store review
    Database-->>BusinessLogic: Confirmation
    BusinessLogic-->>Website: Acknowledge review submission
    Website-->>User: Review submitted successfully
```

Key Interactions:

- Content moderation prevents inappropriate submissions
- Review validation ensures quality standards
- User authentication is verified before submission
- Confirmation feedback improves user experience

## Fetching a List of Places 
 Place search flow based on user-specified criteria. The user enters their criteria via the website, which interacts with business logic to retrieve and display results from the database.

 ```mermaid
 sequenceDiagram
    participant User
    participant Website
    participant BusinessLogic
    participant Database
    
    User->>Website: Connect to the website
    User->>Website: Enter criteria
    Website->>BusinessLogic: Search for places with criteria
    BusinessLogic->>Database: Save criteria
    Database-->>BusinessLogic: Send criteria
    BusinessLogic-->>Website: Display the places with criteria
```
Key Interactions:

- Form validation ensures complete listing information
- Image upload and processing (if applicable)
- Automatic categorization based on listing attributes
- Immediate confirmation provides user feedback


## Conclusion

System Benefits

This architecture provides several key advantages:

- Scalability: Modular design allows independent scaling of components
- Maintainability: Clear separation of concerns facilitates easier updates
- Security: Multiple validation layers ensure data protection
- Performance: Optimized data flow and caching strategies
- Reliability: Robust error handling and transaction management

This technical document serves as the foundation for successful implementation of our HBnB project, providing clear guidelines and ensuring proper architectural decisions during the lifecycle of the project.




## Authors

- [@Sebastien Salgues](https://github.com/SebSa12000)
- [@Elhadj Reziga](https://www.github.com/hedjouj)

