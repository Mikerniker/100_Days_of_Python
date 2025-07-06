# Day 97 Professional Portfolio Project: An Online Shop

https://github.com/user-attachments/assets/fccc45fe-9a09-4d92-b8c2-29fad04e0155

## Overview
- Topics:  Flask, WTForms, Moralis API, Bootstrap, Stripe Integration

### The challenge

- Build an eCommerce website with payment processing. The website needs:
  - A working cart and checkout.
  - It should be able to display items for sale and take real payment from users using Stripe.
  - It should have login/registration authentication features.
 
### Links

- Solution URL: [](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day97)

## Reflection
**Approach, Challenges, Learnings, and Future Improvements:**
This project is a partial start to an eCommerce-style Flask application that integrates Stripe for payments, Moralis for Solana NFTs, and basic login form handling. While it demonstrates core concepts, it does not yet fully satisfy all functional requirements and includes several areas for improvement.

As an initial proof of concept, this project serves as a useful learning exercise. However, for inclusion in a future portfolio, I plan to either evolve it into a fully functional Web3 platform or a more traditional web2 marketplace.

## Concepts Demonstrated

This project demonstrates several key concepts involved in building a modern, eCommerce-style web application with both Web2 and Web3 technologies:

### Web Development with Flask
- Routing with Flask (`@app.route`)
- HTML templating with Jinja2
- Form creation and validation using **Flask-WTF**
- Session handling using Flask’s `session` object

### eCommerce Functionality
- Dynamic product display using external API data (NFTs from Moralis)
- Basic product selection and checkout page
- Integration with **Stripe Checkout** for real payments
- Redirect-based payment flow with success and cancel routes

### Web3 Integration
- Real-time fetching of **Solana NFTs** using Moralis API
- Handling NFT metadata like name, symbol, and image
- Conceptual bridging of NFTs as products in a marketplace

### Authentication Concepts
- Form-based login flow (no database yet)
- Demonstrates structure for future registration/auth system
- Use of Flask forms and basic field validation (e.g., email format, password length)

### Development Concepts
- Use of configuration variables (e.g., `SECRET_KEY`, API keys)
- Environment-style project structure with modular functions
- Proof-of-concept design for extending to a full-stack DApp or marketplace


**Planned Future Enhancements**
To make the project more complete and production-ready, I hope to eventually add the following:

- Implement a user database with registration, login, and logout using Flask-Login. 
- Add a shopping cart system with item add/remove logic.
- Replace random pricing with item-specific pricing logic.
- Store order and payment records (with basic logging at minimum).
- Secure key routes by requiring authentication for checkout.
- If extended as an actual NFT DApp, I would also integrate proper wallet connections, NFT ownership verification, and on-chain transaction support.

For now, this project provides as an initial foundation and review of key concepts, and I look forward to building on it further.

## Notes/Concepts/Review: 


- [Stripe Checkout Quickstart](https://docs.stripe.com/checkout/quickstart)
- [Stripe Checkout Sessions](https://docs.stripe.com/api/checkout/sessions)
- [Stripe API Docs](https://docs.stripe.com/api)
- [Moralis documentation](https://docs.moralis.com/web3-data-api/solana/reference/get-sol-nfts?network=mainnet&address=kXB7FfzdrfZpAZEW3TZcp8a8CwQbsowa6BdfAHZ4gVs&nftMetadata=true&mediaItems=false&excludeSpam=false)
