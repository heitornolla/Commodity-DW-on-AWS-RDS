# dbt-pipeline

# Commodity Data Warehouse Project

## Overview

This project implements a modern Data Warehouse (DW) architecture designed to store and analyze commodity data. We work with an ELT architecture with Postgres and DBT. Data visualization is done with Streamlit.

### Project Steps

1. **Extract & Load**

   - Extracts data from an external **Commodities API**.
   - Loads the data into a **PostgreSQL** database hosted on **AWS RDS**.

2. **Seed Data**

   - Uses DBT seeds to ingest CSV files containing commodity movement data directly into the Data Warehouse.

3. **Transform (DBT Models)**

   - DBT models clean and transform data.
   - Creates **staging** and **datamart** layers in the DW.
   - SQL models: `stg_commodities.sql`, `stg_commodities_transactions.sql`, `dm_commodities.sql`.

4. **Dashboard**
   - Built using **Streamlit**.
   - Displays tables and interactive charts based on transformed data from the Data Warehouse.

---

## Project Architecture (Mermaid Diagram)

```mermaid
graph TD
    A[Commodities API] --> B[Extract]
    B --> C[Load into Postgres - AWS RDS]
    C --> D[Data Warehouse]

    subgraph DBT [Transform - DBT]
        D --> E[stg_commodities.sql]
        E --> F[stg_commodities_transactions.sql]
        F --> G[dm_commodities.sql]
    end

    subgraph Seeds
        H[CSV Files] --> I[DBT Seed]
        I --> D
    end

    G --> K[Streamlit Dashboard]
```
