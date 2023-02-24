# InkThreadable

InkThreadable was created in the frustration over the standardized offerings from the multiple retail stores and the abundance of soulless fashion brands. Our ambition is to offer an amazing variety of designs with excellent quality. The printed t-shirt is a fantastic medium for people to express what they like, who they are and what they identify with. No other garment can be changed and manipulated so easily. No other garment is as strong expression of the individual – that’s why we love t-shirts!

The payment system uses Stripe. Please note that this website is for educational purposes do not enter any personal credit/debit card details when using the site.

To test this system, test card details can be used. A list of these can be found in Stripe's documentation [here](https://stripe.com/docs/testing#cards).

The live link can be found here - [InkThreadable](https://inkthreadable.onrender.com)

## User Experience (UX)

A visitor to InkThreadable would be someone who is most likely a young adult who is interested in vintages T-shirt designs.

### User Stories

#### Viewing and Navigation
- As a Site User, I can intuitively navigate around the site so that I can find content.
- As a Site User, I can view a list of products so that I can select a product to view.
- As a shopper, I can click on a product so that I can read the full product details.
- As a shopper, I can view a specific category of products so I can browse the type of products I'm looking for.
- As a shopper, I can search all products so that I can find what I am looking for.
- As a shopper, I can sort all products so that I can view products based on name, gender and catgory.
- As a shopper, I can add sace items of interest to a wish so i am ble to view and purchace them later.

#### EUser Account and Profile
- As a site user, I can register an account so that I can have a personal account.
- As a site user, I can log in or log out of my account so that I can keep my account secure.
- As a site user, I can save my personal details in my user profile so that I do not have to fill them out for future orders.
- As a site user, I can view my order history so that I can remember what purchases I've made.
- As a site user, I can recover my password in case I forget it so that I can recover access to my account.

#### Purchasing
- As a shopper, I can add a number of products in different quantities to my shopping bag so that I can purchase them all together when I am ready.
- As a shopper, I can view a running total of my shopping bag as I am shopping so that I can see how much it costs in total.
- As a shopper, I can view the contents of my shopping bag at any time so I can see what is included and the total cost.
- As a shopper, I can adjust the quantity of individual products in my bag so that I can easily make changes before I purchase.
- As a shopper, I can see a summary of my shopping cart when I checkout so that I know what products are included and the total cost before I commit to purchasing.
- As a shopper, I can easily enter my payment information securely so that I can purchase my chosen products quickly with no issues.
- As a shopper checkout as a guest so I don't have to sign up for an account.
- As a shopper, I can view an order confirmation after checkout so that I know my purchase was successful.
- As a shopper, I can receive an email confirmation of my order so that I have a record of my purchase.


#### Admin & Store Management

- As a site owner, I can add/edit/delete products through an easy-to-use interface so that I can manage the site's contents.
- As a site owner, I can view and delete customer reviews.

#### User Interaction

- As a site user, I can sign up for the website's newsletter so that I can keep up to date with new products and promotions.


### Design
Through some market research And looking at different sites that offered a similar product i noteiced that they all had farely clean simple designs. My goal was to combine a modern design with a more retro look
They main color pallet for this site is white, black, red and tanned red to get that vintage look.

On the Home page i incorpated a backround that incorporates pop culter/cult classic images to follow the them of the store.


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

## Testing

### Viewing & Navigations

As a Site User, I can intuitively navigate around the site so that I can find content.

### User Account and Profile

As a site user I can register an account so that I can have a personal account.
- A sign up button is located in the My Account drop down menu in the Navbar. When the user clicks the button they are taken to the sign up page.

As a site user I can log in or log out of my account so that I can keep my account secure.*
- If the user has registered an account they can log in or log out by clicking the links in the My Account drop down menu in the header.

As a site user I can save my personal details in my user profile so that I do not have to fill them out for future orders.
- Users can fill in their personal details on their profile page. This information will be prepopulated for any future orders.
- When placing a new order, a checkbox under the delivery information can be checked to save the information just added.

### Purchasing
As a shopper, I can add a number of products in different quantities to my shopping bag so that I can purchase them all together when I am ready.

As shopper I am able to add items to a wishlist so that I can save items of interest.

- Within the product detail page there is a quantity selector and an Add to Bag button. Shoppers can adjust the quantity by using the buttons located on either side of the input, or by typing in the amount.

- When the user clicks on the add to cart button, the chosen quantity of the product is added to the user's shopping cart.

As a shopper I can view a running total of my shopping cart as I am shopping so that I can see how much it costs in total.*

- As the user adds products to their cart, a toast message appears in the top right-hand corner of the screen informing the user that the item has been added.

As a shopper I can view the contents of my shopping cart at any time so I can see what is included and the total cost.

- When the user clicks on the shopping bag icon in the nav bar they are taken to the shopping bag page which shows the products which the user has added to their cart, unit price, quantity and subtotal.

- The bottom of the page shows the cart total, delivery costs and then the grand total.

As a shopper I can adjust the quantity of individual products in my cart so that I can easily make changes before I purchase.

- When the user is viewing the shopping cart, they are able to adjust the quantity of each product line item and update the subtotal by clicking the update icon.

- The user is able to delete the product by clicking the bin icon and the cart should be updated accordingly.

As a shopper, I can see a summary of my shopping cart when I checkout so that I know what products are included and the total cost before I commit to purchasing.

- On the Checkout page the user can see a summary of the line items within their order including a thumbnail image, the product name, the quantity, the unit cost and the overall total order cost.

As a shopper, I can easily enter my payment information securely so that I can purchase my chosen products quickly with no issues.

- When the user navigates to the checkout page, they can see the Stripe Elements UI where they can enter their card details securely and pay for their order.

- The user receives feedback if the card number is valid/invalid.

As a shopper checkout as a guest so I don't have to sign up for an account.
- Shoppers do not need an account to purchase any items. Regardless of whether a user is signed in, the checkout process remains the same.
-  When the user completes the checkout form and presses submit their order should be completed.

As a shopper, I can view an order confirmation after checkout so that I know my purchase was successful.

- When the user submits the checkout form, they are redirected to a Checkout Success page where they can see an order confirmation and a summary of their order.

As a shopper, I can receive an email confirmation of my order so that I have a record of my purchase.

- When the user has submitted their order they will receive a confirmation email to the email address they entered in their order form containing all the details of the order.

### Admin & Store Management
As a store owner, I can add/edit/delete products through an easy-to-use interface so that I can manage the store's contents.

- When the site owner is logged in, aM anagement option appears in the My Account drop-down menu.
- When the site owner navigates to the Management page they can add a new product to the store through a user-friendly form.

- The site owner is able to edit and delete products by clicking buttons on both the product page and also the product detail page.
- The edit form is pre-populated with the product information.

### EPIC | User Interaction
As a site user, I can signup to a newsletter the form is located in the footer. 
- A user can access the contact form by clicking on the contact us button on the footer.


## Device Testing

The website was viewed on a variety of devices such as Desktop, Laptop, iPhone 8, iPhoneXR and iPad to ensure responsiveness on various screen sizes in both portrait and landscape mode. The website performed as intended. The responsive design was also checked using Chrome developer tools across multiple devices with structural integrity holding for the various sizes.

## Browser Testing

The Website was tested on Google Chrome, Firefox, Safari browsers with no issues noted.





