# Easy Report: eCommerce Company Dashboard Project
## 1. Background
  An e-commerce company that has recently opened in Brazil wishes to track the company's progress. Monitoring activities, as a new company, become a reference in order to provide an overview of how far the company is running and what needs to be improved and made improvements. Several datasets from various departments, such as sales, marketing, and bus dev, were already owned, so the company hired a BI Analyst to process the existing datasets and then present them in the form of an comprehensive dashboard to assist company leaders in monitoring the recent findings.
## 2. Objective
### 2.1 Project Objective
“Easy understanding for the next decision making”
Creating a single-sourced Dashboard that contains dedicated pages for the Sales, Marketing, and Business Development department. The dashboard is intended to give an overview from each department’s performance so the executive level can take action to encourage, maintain, or perform corrective action to the respective department.

### 2.2 Inisiative
a) Create a company-wide dashboard to monitor activities from the Sales, Marketing, and Business Development Department.

b) Each Department would have their own dedicated Dashboard.

c) Dashboards should be easy to use, compact, and give a clear picture of each department's performance.

### 2.3 User Persona
**a) C-Level (Management)**
  * What they do
    - Oversee all business operations and decisions and are responsible for the success of the organization
  * What they need:
    - Overview performance sales, marketing, bis dev department
    - Clear information, compact, easy to understand within 5 minutes of reading.

**b) Business Development Dept**
  * What they do:
    - Identifying and taking advantage of growth opportunities.
  * What they need:
    - Visual report of a/b testing result that they have conducted
    
**c) Marketing Dept.**
  * What they do:
    - Reach out to prospects, customers, investors and/or the community, while creating an overarching image that represents your company in a positive light.
  * What they need:
    - Presenting which target market has the greatest potential per period, as well as recommendations for the next target market to target based on existing data.
    - percentage of purchase compare to visit
    - Progress to see percentage campaign achievement

**d) Sales Dept.**
  * What they do:
    - Overseeing what the sales team is doing, making plans and setting targets. It also includes generally ensuring the efficiency of the sales process to get the best result for the business
  * What they need:
    - Allows sales management and clients to easily track data sources and see whether sales forecasts are being met.
    - Having a clear and reliable data set means there will be better decision-making

## 3. Overview Process
### a) Data Extracting
  We have several datasets that are given from several departments that we can get some information to analyze the data. We proposed a comprehensive dashboard to c-level that will help the organization thrive. There the list of dataset below:
* Sales Dataset
    - Order list dataset
    - Order Item dataset
    - Order review dataset
    - Order customer dataset
    - Order seller dataset
    - Order product dataset
* Marketing Dataset
* BizDev - A/B testing Dataset
* Data schema

![data schema](https://user-images.githubusercontent.com/102814373/193418657-1fe5ff7c-bcab-4b5e-a22c-1d5f0c227ca7.png)


### b) Data Cleaning and Processing
* Change the (_) in the product category column to a space
* use the Python translators library to translate the category name from Portuguese to English.
### c) Data Wrangling for A/B testing
* Verify that the control group with the old page and the treatment group with the new page, and then delete the rest that do not match.
* converting daily data into a cumulative total.
* Added conversion rate column on table
* Import the library stats model to find the p value and power per day.

### d) Visualization with Tableau
* Added a shapefile to create a map visualization of Brazil and connected with existing datasets.

### 3.1 User Flow
* Simple usage
    - Similar user-flow for all department
    - Adjust step in choosing department page and filters
* Intuitive timeframe filters
    - Data on dashboard adapts based on adjustment in date/year filters
* Open to Improvement
    - Dashboard is always open for requests based on each department needs
      Request will be queued on BI team pipeline

![User flow](https://user-images.githubusercontent.com/102814373/193417612-967c1655-551a-402b-ab5d-2ee320e33990.png)

### 3.2 MVP - Dashboard
a) Sales Dahsboard
![Sales dashboard](https://user-images.githubusercontent.com/102814373/193417347-cb9a0c05-a3ed-4d30-b6dc-608f886957ae.png)


b) Marketing Dashboard

![marketing dashboard](https://user-images.githubusercontent.com/102814373/193417419-663fb988-1b66-49e2-a6f2-01a2537bcbe0.png)



c) Bus Dev Dashboard

![ab test dashboard](https://user-images.githubusercontent.com/102814373/193417444-1fdcafba-5d59-4d77-ae12-604da9432708.png)


## 4. Analysis and Result
The final dashboard presents a rough overview of each department’s activities and needs. Within this subchapter, we would like to elaborate more regarding dashboard analysis in order to answer each department’s inquiries regarding the data.
### 4.1 Sales Dashboard Analisis
* The C-Levels noticed that there is a slight drop of total sales in the current quarter than in the last quarter. What steps could the company take to have an increase in sales in this quarter?
    - First, let’s analyze the dashboard and look for certain information comparing the current quarter and the last quarter.
    - By comparing the [Late delivery%] and [Late shipment%] in the current quarter and the last quarter, by using the [Timeframe] filter from April 2018 to August 2018, it shows that there is an increase of % in the current quarter. The company can take steps to evaluate the operational processes of delivery, including the carrier partner performance. 
    - By clicking on the category, the [Running Sales per Quarter] time series chart can show how each category performs in each quarter. Clicking on the category ‘Health and Beauty’ and ‘Telephone’ shows that this Category has an increase of sales in this quarter than the last quarter. Looking at the table [User/Seller Stat], reader can see which city has the most User or Seller. 
    - From the data above the company can focus on doing more sales in the categories that have a higher sales in this quarter. From focusing on doing advertising in those categories and also doing collaboration with sellers in certain cities that yield higher sales.

### 4.2 Marketing Dashboard Analisis
* Why is the [Age Group] divided by 10 years instead of Generation/Era?
    - Due to many interpretations regarding Generation and birth year, and in order to minimize misunderstanding, the B.I. Team decided to group user birth years by 10 years each.
* How could the dashboard help the Marketing Dept. in planning a reactivation campaign for users who have been inactive for more than 7 days?
    - Aim cursor to [Purchase Recency] table. Select the rows for “Last 14 Days” and “Last 30 Days”. Wait for the dashboard to load information.
    - For more detailed planning, use [Age Filter] to select certain age groups.
* How come there are no dedicated Recency, Frequency, and Monetary Value (RFM) charts within the dashboard?
    - In order to increase visibility of the actual data, minimize steps-needed to access information, and to synchronize the [Age Group] filter for the whole dashboard, the B.I. team decided to break down RFM into dedicated parts.
    - “Recency” and “Frequency” could be viewed on [Purchase Recency] chart;
    - Overall view of “Monetary Value” could be viewed on [Overall Avg. Spending per Category] and a more detailed view per Age Group could be viewed in [Avg. Spending Per Age Group] chart.


### 4.3 Bus Dev Dashboard Analisis
After BI team present dashboard, the a/b test result uses statistical tests to determine the significance value of the existing landing page tests based on the dataset provided by the bus dev team.
Team BI get p value of 0.189 was obtained from statistical tests conducted for January cumulative data for a total of 294,475 consumers with a total of 24 days, which is greater than 0.05, indicating that the old landing page test and the new landing page test do not have a significant difference.


## 5. Reference
Dataset:

[Sales Department Dataset](https://drive.google.com/drive/folders/1xql56CMrIKNppRjQOF61wNKTPmTMr46z?). Google Drive. Public View. 

[Marketing Department Dataset](https://drive.google.com/drive/folders/1zDGgc7OmBccFg-ENPjeeRPCZ1fX6X-so?). Google Drive. Public View. 

[BizDev A/B Testing Dataset](https://drive.google.com/drive/folders/1eUI8J0IrjBDKKz-7OGp75uuX3_AdL7hU?). Google Drive. Public View. 

[Dashboard Creation](https://docs.google.com/document/d/1Su31q3W03MM_0LZlT8ac2_SIVZWW0VZ3cF17x9nemvY/): Dashboard Dataset & Variable Notes. Google Docs. Public View. 

[Dashboard Mockup](https://docs.google.com/presentation/d/14sFWUY8cU0aQnLn9lt9tJanYAYe2VultjFz1YZvGIqo/). Google Slideshow. Public View.


Final Product:

[eCommerce Dashboard](https://public.tableau.com/app/profile/larasati.prabowo/viz/PLBI2eCommerceDashboardTimL/DashboardMarketing). Tableau Public. Public View. 
