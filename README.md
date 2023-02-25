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

### Wireframes

#### Home Page
![wireframes image](/media/home.png)

#### Product Page
![wireframes image](/media/products.png)

#### Cart Page
![wireframes image](/media/cart.png)

#### Product Detail Page
![wireframes image](/media/about.png)

## Agile Methodology
Github projects was used to manage the development process using an agile approach. Please see link to project board [here]()


The Epics listed above were documented within the Github project as Milestones. A Github Issue was created for each User Story which was then allocated to a milestone(Epic). Each User Story has defined acceptance criteria to make it clear when the User Story has been completed.

## Database Schema 

Two relational databases were used to create this site - during production SQLite was used and then Postgres was used for the deployed Render version. Below is an image of how the database models relate to each other:

![Database Schema](/media/inkthreadable.png)

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

The website was viewed on a variety of devices such as Desktop, Laptop, iPhone 8, iPhoneXR and iPad to ensure responsiveness on various screen sizes. The website performed as intended. The responsive design was also checked using Chrome developer tools across multiple devices with structural integrity holding for the various sizes.

## Browser Testing

The Website was tested on Google Chrome, Firefox, Safari browsers with no issues noted.


## Validator Testing

### HTML
All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/). See results in below table.

| Page                           | Logged Out | Logged In |
|--------------------------------|------------|-----------|
| Home                           | No Errors  | No Errors |
| Products                       | No Errors  | No Errors |
| Product Detail                 | No Errors  | No Errors |
| Add Product                    | N/A        | Note      |
| Edit Product                   | N/A        | Note      |
| Delete Product                 | N/A        | No Errors |
| wishlist                       | N/A        | No Errors |
| cart                           | No Errors  | No Errors |
| Checkout                       | No Errors  | No Errors |
| Checkout Success               | No Errors  | No Errors |
| Profile                        | N/A        | No Errors |
| Contact                        | No Errors  | No Errors |
| About                          | N/A        | No Errors |
| Sign In                        | No Errors  | N/A       |
| Sign Up                        | No Errors  | N/A       |
| Log Out                        | N/A        | No Errors |
| Password Reset                 | No Errors  | N/A       |
| 404.html                       | No errors  | No errors |
|_________________________________________________________|
Note: Image upload widget errors

Forms that include an image upload field show the same error below. This relates to the image upload widget on the form.

### CSS

No errors were found when passing my CSS files through the official [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

-base.css: Congratulations! No Error Found.

-checkout.css: Congratulations! No Error Found.

-profile.css: Congratulations! No Error Found.

### JSHINT
All Javascript was passed through [Jshint](https://jshint.com/) with no issues.

**Base**
- No errors detected

**Products**
- No errors detected

**Profile**
- No errors detected

**Checkout**
- No errors detected

**cart**
- No errors detected

**Quantity Input**
-No Errors detected

**Image Selector**
-No errors detected

### Python Validation
Python testing was done using  [Python syntax checker](https://extendsclass.com/python-tester.html) to ensure there were no syntax errors.

The only errors displayed can be ignored. The majority are in automatically generated files with the exception of env.py and webhooks.py. 

I have ignored the the formatting errors related to env.py as they relate to my Secret Keys and Database URL being to long. This file is not committed to github.


### Lighthouse

Lighthouse validation was run but would not complete the process and timeout due to an error with light house. This was attempted a few times with the same result. I have never seen this before on any of my previous projects. It may be due to my Interenet. AS I am in Liberia West Africa at the moment, the interenet provided is increadably slow.
My hand in is today and I have not been able to resolve this problem.


## Manual Testing

### Home Page

| Element                | Action | Expected Result                    | Pass/Fail |
|------------------------|--------|------------------------------------|-----------|
| Shop Now Button        | Click  | Open products page                 | Pass      |



### All Auth Pages 



| Element                         | Action                                    | Expected Result                              | Pass/Fail |
|---------------------------------|-------------------------------------------|----------------------------------------------|-----------|
| Sign Up                         |                                           |                                              |           |
| Sign in link                    | Click                                     | Redirect to sign in page                     | Pass      |
| Email field                     | Insert incorrect format                   | On submit: form won't submit                 | Pass      |
| Email field                     | Insert incorrect format                   | Error message displays                       | Pass      |
| Email field                     | Insert correct format                     | On submit: form submit                       | Pass      |
| Email field                     | Leave empty                               | On submit: form won't submit                 | Pass      |
| Email field                     | Insert duplicate email                    | On submit: form won't submit                 | Pass      |
| Email field                     | Insert duplicate email                    | Error message displays                       | Pass      |
| Email Confirmation field        | Insert different email                    | On submit: form won't submit                 | Pass      |
| Email Confirmation field        | Insert different email                    | Error message displays                       | Pass      |
| Username field                  | Leave empty/incorrect format              | On submit: form won't submit                 | Pass      |
| Username field                  | Leave empty/incorrect format              | Error message displays                       | Pass      |
| Username field                  | Insert correct format                     | On submit: form submit                       | Pass      |
| Username field                  | Insert duplicate username                 | On submit: form won't submit                 | Pass      |
| Username field                  | Insert duplicate username                 | Error message displays                       | Pass      |
| Password field                  | Insert incorrect format/length            | On submit: form won't submit                 | Pass      |
| Password field                  | Insert incorrect format/length            | Error message displays                       | Pass      |
| Password field                  | Passwords don't match                     | On submit: form won't submit                 | Pass      |
| Password field                  | Passwords don't match                     | Error message displays                       | Pass      |
| Password field                  | Insert correct format and passwords match | On submit: form submit                       | Pass      |
| Sign Up button(form valid)      | Click                                     | Form submit                                  | Pass      |
| Sign Up button(form valid)      | Click                                     | Redirect to Verify Email Address page        | Pass      |
| Sign Up button(form valid)      | Click                                     | Alert message confirming email sent appears  | Pass      |
| Confirmation Email Confirm Link | Click                                     | Open Confirm Email Address Page              | Pass      |
| Confirm Button                  | Click                                     | Success message confirming new user appears  | Pass      |
| Confirm Button                  | Click                                     | Redirect to sign in page                     | Pass      |
|                                 |                                           |                                              |           |
| Log in                          |                                           |                                              |           |
| Sign up link                    | Click                                     | Redirect to sign up page                     | Pass      |
| Username field                  | Leave empty                               | On submit: form won't submit                 | Pass      |
| Username field                  | Leave empty                               | Error message displays                       | Pass      |
| Username field                  | Insert wrong username                     | On submit: form won't submit                 | Pass      |
| Username field                  | Insert wrong username                     | Error message displays                       | Pass      |
| Password field                  | Leave empty                               | On submit: form won't submit                 | Pass      |
| Password field                  | Leave empty                               | Error message displays                       | Pass      |
| Password field                  | Insert wrong password                     | On submit: form won't submit                 | Pass      |
| Password field                  | Insert wrong password                     | Error message displays                       | Pass      |
| Login button(form valid)        | Click                                     | Form submit                                  | Pass      |
| Login button(form valid)        | Click                                     | Redirect to home page                        | Pass      |
| Login button(form valid)        | Click                                     | Success message confirming login appears     | Pass      |
| Forgot Password Link            | Click                                     | Redirect to Password Reset page              | Pass      |
| Email field                     | Leave empty/incorrect format              | On submit: form submit                       | Pass      |
| Reset My Password Button        | Click                                     | Confirmation message that email sent         | Pass      |
| Password Reset Email Link       | Click                                     | Open Change Password Page                    | Pass      |
| Change Password Button          | Click                                     | Success message confirming Password Changed  | Pass      |
|                                 |                                           |                                              |           |
| Sign Out Confirmation           |                                           |                                              |           |
| Sign Out  button                | Click                                     | Redirect to homepage                         | Pass      |
| Sign Out  button                | Click                                     | Success message confirming Sign Out  appears | Pass      |

### Products

| Element                         | Action  | Expected Result                                                                                | Pass/Fail |
|---------------------------------|---------|------------------------------------------------------------------------------------------------|-----------|
| Sort By' gender and category    | Click   | Open 'sort by' options                                                                         | Pass      |
| If Category Selected            | Display | Pages heading changes to show items assigned the category selected                             | Pass      |
| Product Number                  | Display | Displays correct number of products on page                                                    | Pass      |
| Product Card                    | Click   | Redirect to product detail page                                                                | Pass      |
| If Searched Product             | Display | Only display products with search term in title                                                | Pass      |
| If Searched Product             | Display | Display number of products found for " searched product"                                       | Pass      |
| If Superuser in session:        |         |                                                                                                |           |
| Delete product link             | Click   | Open delete confirmation  page                                                                 | Pass      |
| Confirm Delete -  delete button | Click   | Delete product                                                                                 | Pass      |
| Confirm Delete -  delete button | Click   | Success message appears confirming product deleted successfully                                | Pass      |


### Product Detail

| Element                  | Action                    | Expected Result                                                                              | Pass/Fail |
|--------------------------|---------------------------|----------------------------------------------------------------------------------------------|-----------|
| Product Content          | Display                   | Display correct product image, description, category, gender, price, product details         | Pass      |
| Keep Shopping button     | Click                     | Redirect to home decor page                                                                  | Pass      |
| Add to cart button       | Click                     | Add item to bag                                                                              | Pass      |
| Add to cart button       | Click                     | Toast Success appears                                                                        | Pass      |
| Add to cart button       | Click                     | Product and quantity visible in toast success                                                | Pass      |
| If Superuser in session: |                           |                                                                                              |           |
| Edit product link        | Click                     | Redirect to edit product page                                                                | Pass      |
| Delete product link      | Click                     | Open delete confirmation  page                                                               | Pass      |
| Add to wishlist.         | Click                     | Add product to wishlist.                                                                     | Pass      |

### Cart

| Element                                                       | Action              | Expected Result                                        | Pass/Fail |
|---------------------------------------------------------------|---------------------|--------------------------------------------------------|-----------|
| No cart Items                                                 |                     |                                                        |           |
| Keep Shopping button                                          | Click               | Redirect to home decor page                            | Pass      |
| cart Items                                                    |                     |                                                        |           |
| Qty control buttons                                           | Click               | Increase/decrease quantity                             | Pass      |
| Qty control buttons                                           | Click               | Minus button disabled if quantity is 1                 | Pass      |
| Qty control buttons                                           | Click               | Plus button disabled if quantity is 99                 | Pass      |
| Qty control buttons                                           | Manually Input  >99 | Error message appears when refresh button is clicked   | Pass      |
| Qty control buttons                                           | Manually Input  <1  | Shopping bag is emptied when refresh button is clicked | Pass      |
| update button                                                 | Click               | Update bag item quantity                               | Pass      |
| update button                                                 | Refresh Icon button | Updated confirmation toast appears                     | Pass      |
| remove button                                                 | Click               | Remove item from bag                                   | Pass      |
| remove button                                                 | Click               | Removed confirmation toast appears                     | Pass      |
| Line item subtotal / cart total / Delivery cost / Grand Total | Calculate           | All numbers are calculated correctly                   | Pass      |
| Continue shopping button                                      | Click               | Redirect to products page                              | Pass      |
| Secure Checkout button                                        | Click               | Redirect to checkout page                              | Pass      |

### Profile

| Element                | Action            | Expected Result                                                                                                                | Pass/Fail |
|------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------|
| Open Profile Page      | Access            | If a user tries to access the profile page (by changing the url) without being signed in they are redirected to the login page | Pass      |
| Form fields            | On load           | fields populated with user default info(if previously saved)                                                                   | Pass      |
| All input fields       | Leave blank       | On submit: form submits                                                                                                        | Pass      |
| All input fields       | Just whitespace   | On submit: form submits                                                                                                        | Pass      |
| All input fields       | Fill in correctly | On submit: form submits                                                                                                        | Pass      |
| Form Dropdown          | Click             | Show dropdown options                                                                                                          | Pass      |
| Update button          | Click             | Form submits                                                                                                                   | Pass      |
| Update button          | Click             | Success message appears confirming profile successfully updated                                                                | Pass      |

## Deployment

### Deployment On Render

- To Deploy on render I connected my git hub account to Render.

- I then selected the repositry and conntected it to render.

- Added my environment variables.


- created a build.sh file
- installed gunicorn

- Then automatically deploy my local site to render.

### Attach Postgress Database
Copy the DATABASE_URL located in Config Vars in the Settings Tab.
Go back to your IDE and install 2 more requirements:

- pip3 install dj_databse_url
- pip3 install psycopg2-binary

Create requirements.txt file by typing pip3 freeze --local > requirements.txt
Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
In settings.py file import dj_database_url, comment out the default configurations within database settings and add the following:
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

- Run migrations and create a superuser for the new database.
- Create an if statement in settings.py to run the postgres database when using the app on render or sqlite if not
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
    }
Create requirements.txt file by typing pip3 freeze --local > requirements.txt

Create a file named "Procfile" in the main directory and add the following: web: gunicorn project-name.wsgi:application


Push these changes to Github

-