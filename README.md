# InkThreadable

InkThreadable was created in the frustration over the standardized offerings from the multiple retail stores and the abundance of soulless fashion brands. Our ambition is to offer an amazing variety of designs with excellent quality. The printed t-shirt is a fantastic medium for people to express what they like, who they are and what they identify with. No other garment can be changed and manipulated so easily. No other garment is as strong expression of the individual – that’s why we love t-shirts!

The payment system uses Stripe. Please note that this website is for educational purposes do not enter any personal credit/debit card details when using the site.

To test this system, test card details can be used. A list of these can be found in Stripe's documentation [here](https://stripe.com/docs/testing#cards).

The live link can be found here - [InkThreadable](https://inkthreadable.onrender.com)

## User Experience (UX)

A visitor to InkThreadaböe would be someone who is most likely a young adult who is interested in vintages T-shirt designs.

### User Stories

#### EPIC | Viewing and Navigation
- As a Site User, I can intuitively navigate around the site so that I can find content.
- As a Site User, I can view a list of products so that I can select a product to view.
- As a shopper, I can click on a product so that I can read the full product details.
- As a shopper, I can view a specific category of products so I can browse the type of products I'm looking for.
- As a shopper, I can search all products so that I can find what I am looking for.
- As a shopper, I can sort all products so that I can view products based on name, gender and catgory.
- As a shopper, I can add sace items of interest to a wish so i am ble to view and purchace them later.

#### EPIC | User Account and Profile
- As a site user, I can register an account so that I can have a personal account.
- As a site user, I can log in or log out of my account so that I can keep my account secure.
- As a site user, I can save my personal details in my user profile so that I do not have to fill them out for future orders.
- As a site user, I can view my order history so that I can remember what purchases I've made.
- As a site user, I can recover my password in case I forget it so that I can recover access to my account.

#### EPIC | Purchasing
- As a shopper, I can add a number of products in different quantities to my shopping bag so that I can purchase them all together when I am ready.
- As a shopper, I can view a running total of my shopping bag as I am shopping so that I can see how much it costs in total.
- As a shopper, I can view the contents of my shopping bag at any time so I can see what is included and the total cost.
- As a shopper, I can adjust the quantity of individual products in my bag so that I can easily make changes before I purchase.
- As a shopper, I can see a summary of my shopping cart when I checkout so that I know what products are included and the total cost before I commit to purchasing.
- As a shopper, I can easily enter my payment information securely so that I can purchase my chosen products quickly with no issues.
- As a shopper checkout as a guest so I don't have to sign up for an account.
- As a shopper, I can view an order confirmation after checkout so that I know my purchase was successful.
- As a shopper, I can receive an email confirmation of my order so that I have a record of my purchase.


#### EPIC | Admin & Store Management

- As a site owner, I can add/edit/delete interior design services provided through an easy-to-use interface so that I can manage the site's contents.
- As a site owner, I can add/delete images and location of previous design projects so that I can manage the site's contents.
- As a site owner, I can view and delete customer reviews.

#### EPIC | User Interaction

- As a site user, I can sign up for the website's newsletter so that I can keep up to date with new products and promotions.

## Agile Methodology
Github projects was used to manage the development process using an agile approach. Please see link to project board [here]()


The Epics listed above were documented within the Github project as Milestones. A Github Issue was created for each User Story which was then allocated to a milestone(Epic). Each User Story has defined acceptance criteria to make it clear when the User Story has been completed.

## Database Schema 

Two relational databases were used to create this site - during production SQLite was used and then Postgres was used for the deployed Render version. Below is an image of how the database models relate to each other:

![Database Schema](docs/readme_images/database_schema.png)

## Security Features and Defensive Design
### User Authentication

Where I have used Django's Class-based-views; Django's LoginRequiredMixin is used to make sure that any requests to access secure pages by non-authenticated users are redirected to the login page. Django's UserPassesTestMixin is used to limit access based on certain permissions.

Where I have used function based views I have used Django's login_required to restrict access as required. 

### Form Validation
If incorrect or empty data is added to a form, the form won't submit and a warning will appear to the user informing them what field raised the error.

### Database Security
The database url and secret key are stored in the env.py file to prevent unwanted connections to the database. Stripe keys and wh secret are also stored in the env.py file. 

Cross-Site Request Forgery (CSRF) tokens were used on all forms throughout this site.

## Features