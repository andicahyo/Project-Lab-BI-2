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
### 4.2 Marketing Dashboard Analisis
### 4.3 Bus Dev Dashboard Analisis
After BI team present dashboard, the a/b test result uses statistical tests to determine the significance value of the existing landing page tests based on the dataset provided by the bus dev team.
Team BI get p value of 0.189 was obtained from statistical tests conducted for January cumulative data for a total of 294,475 consumers with a total of 24 days, which is greater than 0.05, indicating that the old landing page test and the new landing page test do not have a significant difference.


## 5. Reference
Dataset:
Sales Department Dataset. Google Drive. Public View. https://drive.google.com/drive/folders/1xql56CMrIKNppRjQOF61wNKTPmTMr46z?

Marketing Department Dataset. Google Drive. Public View. https://drive.google.com/drive/folders/1zDGgc7OmBccFg-ENPjeeRPCZ1fX6X-so?

BizDev A/B Testing Dataset. Google Drive. Public View. https://drive.google.com/drive/folders/1eUI8J0IrjBDKKz-7OGp75uuX3_AdL7hU?

Dashboard Creation:
Dashboard Dataset & Variable Notes. Google Docs. Public View. https://docs.google.com/document/d/1Su31q3W03MM_0LZlT8ac2_SIVZWW0VZ3cF17x9nemvY/

Dashboard Mockup. Google Slideshow. Public View. https://docs.google.com/presentation/d/14sFWUY8cU0aQnLn9lt9tJanYAYe2VultjFz1YZvGIqo/

Final Product:
eCommerce Dashboard. Tableau Public. Public View. https://public.tableau.com/app/profile/larasati.prabowo/viz/PLBI2eCommerceDashboardTimL/DashboardMarketing
