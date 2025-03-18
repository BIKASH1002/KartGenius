# KartGenius: Your Smart Shopping Companion

In today’s digital world, shopping online for gifts or personal use can be both convenient and overwhelming. With countless products, reviews, and price points scattered across multiple sites, finding the perfect item can turn into a time-consuming challenge. People often face decision fatigue after hours of browsing and comparing options. KartGenius was created to tackle these challenges by streamlining product searches and comparisons, helping users quickly pinpoint the best choices without the hassle.

## Content

- [Overview](#overview)

- [Setup](#setup)

- [Data](#data)

- [Features](#features)

- [Procedure](#procedure)

- [Workflow](#workflow)

- [User Interface](#user-interface)

- [Conclusion](#conclusion)

## Overview

KartGenius is a web-based shopping assistant built with Flask. It refines user queries and fetches product data from SerpAPI, displaying a clear, side-by-side comparison table using Pandas. Originally developed as a guided project from IBM’s Cognitive Class, KartGenius has been enhanced with custom features like favourites, recent searches and product image view to provide a more engaging, interactive experience. This project simplifies the process of comparing products, saving users both time and effort.

## Setup

- **Visual Studio Code:** for developement

- **Flask:** for web-framework

- **SerpAPI:** for fetching real-time product data

## Data

All product information is dynamically fetched from SerpAPI based on user queries.

## Features

- **Query Refinement:** Improves raw user input to form a better search query.

- **Product Search:** Retrieves product data from SerpAPI based on the refined query and location.

- **Comparison Table:** Generates a side-by-side table of products using Pandas.

- **Favourites Modal:** Allows users to save their favorite products locally.

- **Recent Searches Modal:** Displays a list of the user's recent search queries.

- **Clean UI:** A modern, user-friendly interface that makes product comparisons easy.

## Procedure

**1. Input Stage:**

- The user navigates to the home page.

- They enter a product query (e.g., "gift ideas") and optionally a location (e.g., "New York" or "Mumbai").

**2. Query Refinement:**

- The raw query is processed by a refinement function that normalizes and optimizes the input.

**3. Product Fetching:**

- The refined query is sent to SerpAPI to fetch relevant product data.

- The API returns a list of products along with details like price, rating, and reviews.

**4. Data Processing:**

- The application uses Pandas to process the fetched data.

- A comparison table is generated, displaying products side by side with key details.

**5. Displaying Results:**

- The refined query, along with the comparison table and a summary, is rendered on the homepage.

- Additional features (favourites and recent searches) are available via interactive modals.

**6. User Interaction:**

- Users can add products to their favourites for later review.

- They can also view and select from recent searches to quickly redo a query.

- The UI updates dynamically, providing a seamless experience.

## Workflow

<div align = "center">
  <img src = "https://github.com/user-attachments/assets/47fda1a9-c589-4cd6-b7b1-83dd4e4f7838" alt = "Workflow" >
</div>

## User Interface

<div align = "center">
  <img src = "https://github.com/user-attachments/assets/0da58181-49f9-440a-86a5-826f2e7a934b" alt = "Aspect sentiment" width = 50%>
</div>

<div align = "center">
  <img src = "https://github.com/user-attachments/assets/bfa611e2-f6e5-4d9b-9a69-c82370de5814" alt = "Aspect sentiment" width = 50%>
</div>

<div align = "center">
  <img src = "https://github.com/user-attachments/assets/17753f9f-50ec-4935-b40c-a733e0610df7" alt = "Aspect sentiment" width = 50%>
</div>

## Conclusion

KartGenius streamlines the online shopping experience by refining search queries and providing a clear product comparison table. Originally built as part of IBM’s Cognitive Class, it now includes custom features like favourites and recent searches, making it a versatile tool for anyone looking to shop smarter. This project not only simplifies product discovery but also demonstrates how AI-inspired enhancements can elevate everyday tasks.
