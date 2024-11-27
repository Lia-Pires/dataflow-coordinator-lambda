# DataFlow Coordinator

## Overview

**DataFlow Coordinator** is a serverless solution designed to process and route dynamic payloads to the appropriate database tables using **AWS Lambda**. Triggered by events from **Amazon SQS**, the Lambda function processes incoming messages and determines which tables need to be updated based on the data within the payload. This architecture offers flexibility and scalability, allowing you to easily manage data updates without complex infrastructure management.

## Features

- **Event-Driven**: Processes data in real-time with AWS Lambda, triggered by messages from **Amazon SQS**.
- **Scalable**: Automatically scales based on the number of messages in the SQS queue, minimizing operational overhead.
- **Flexible**: Handles various types of data payloads and dynamically routes them to the correct tables.
- **Easy Integration**: Seamlessly integrates with other AWS services like **SNS**, **API Gateway**, and **RDS**.
- **Minimal Configuration**: Organizes payloads and updates tables with minimal manual intervention, reducing complexity.

## Architecture

- **AWS Lambda**: Processes payloads from the SQS queue and directs them to the appropriate database tables.
- **Amazon SQS**: The event source that triggers the Lambda function, delivering payloads in the form of messages.
- **Database**: Relational database (e.g., **AWS RDS**, **Aurora**) where the data is stored and updated. Tables include entities such as `Customers`, `Purchases`, `Products`, etc.

## Use Cases

### 1. **Customer Updates**
Automatically updates customer details, such as:
- **Personal Information**: Name, email, contact details.
- **Address Management**: Shipping and billing addresses.
- **Subscription/Preferences**: Subscription plans, marketing preferences.

**Payload Example**:

```json
    {   
        "customer_update": true,
        "address_update" : true,
        "customer_id": 1,
        "name": "Lia Pires",
        "email": "lia.pires@example.com",
        "phone" : "+5545999999999",
        "birth_date" : "1992-09-15" ,
        "address_id" : 1 ,
        "registration_date" : "2024-11-24 14:30:00",
        "active" : true ,     
        "shipping_address": {            
            "street": "Main St",
            "number" : "245",
            "complement" : "Next to the Post Office",
            "city": "Anytown",
            "state" : "Anystate",
            "country" : "Anycountry",
            "neighborhood" : "That Neighborhood",
            "postal_code": "67890-1234"
    }
    }
```


### 2. **Purchase Processing**
Handles the creation and updating of purchase transactions, including:

- **Order Details**: Items, quantities, prices.
- **Payment Information**: Total amounts, status (paid, pending).
- **Order Status Updates**: Shipping, delivery, and returns.

**Payload Example**:

```json
    {    
        "purchase_id": 456,
        "customer_id": 123,
        "purchase_date" : "2024-11-24 14:30:00",
        "items": [
            {   
                "item_id" : 1,
                "product_id": 789,
                "quantity": 2,
                "unit_price": 99.99
            },
            {   
                "item_id" : 2,
                "product_id": 452,
                "quantity": 3,
                "unit_price": 25.50
            }
        ],
        "total_amount": 276.48,
        "status": "paid"
    }
```






### 3. **Product Management**
Easily updates product catalogs with:

- **Stock Levels**: Quantity, availability.
- **Price Updates**: New price, discounts.
- **Product Attributes**: Description, categories, specifications.

### Payload Example:
```json
    {   
        "product_id": 789,
        "name": "Wireless Mouse",
        "product_description" : "A compact, ergonomic device offering seamless connectivity, precision tracking, and long-lasting battery life. Ideal for both work and gaming, it features a sleek design and compatibility with multiple devices via Bluetooth or a USB receiver",
        "unit_price": 49.99,
        "stock_quantity": 150,       
        "category": "Electronics"
    }
```

### 4. **User Activity Tracking**
Tracks user interactions and activity, such as:

- **Login Events**: Timestamp, IP address, device used.
- **Behavioral Analytics**: Product views, cart additions, clickstream data.

### Payload Example:

```json
    {   
        
        "customer_id": 123,
        "interaction_id" : 123,
        "preference_id" : 123,
        "category" : 123,
        "notifications" : false,
        "interaction_type" : "login",
        "interaction_date" : "2024-11-23T10:15:00Z",
        "interaction_description" : "User logged in from ip 192.168.1.100",
        "device" : "mobile",
        "ip_address": "192.168.1.100"
    }
```


### 5. **Inventory and Stock Management**
Monitors and updates inventory levels based on:

- **Stock Restocks**: New inventory shipments.
- **Stock Movements**: Item transfers between warehouses, returns.
- **Low Stock Alerts**: Trigger notifications when stock falls below a threshold.

### Payload Example:
```json
    {
        "product_id": 789,
        "restocked_quantity": 100,
        "restock_date" : "2024-11-23T10:15:00Z"
    } 
```


## Installation

### Prerequisites
- **AWS Account**: Ensure you have an AWS account with Lambda, SQS, and database access.
- **AWS CLI**: Installed and configured for deployment.
- **Node.js/Python**: Depending on your Lambda function language (adjust accordingly).

### Steps to Deploy

1. **Clone this repository**:
    ``` bash
    git clone https://github.com/lia-pires/dataflow-coordinator-lambda.git
    cd dataflow-coordinator-lambda
    ```
    

2. **Configure AWS credentials**: Make sure your AWS credentials are set up using the AWS CLI or environment variables.

3. **Create an SQS Queue**:  
   Create an SQS queue that will trigger the Lambda function when new messages arrive.

   Example (using AWS CLI):


    ```bash
    aws sqs create-queue --queue-name dataflow-queue
    ```

4. **Deploy Lambda**:
   Deploy the Lambda function using AWS SAM, Serverless Framework, or CloudFormation.
   Configure the Lambda function to be triggered by the SQS queue you created.

5. **Test the Lambda function**:
   Send test messages to the SQS queue and confirm that the Lambda function processes them and updates the correct database tables.

## Configuration

### Environment Variables
The following environment variables are required for Lambda to connect to the database and handle dynamic payloads:

- **DB_HOST**: Hostname of the database.
- **DB_USER**: Database username.
- **DB_PASSWORD**: Database password.
- **DB_NAME**: The database name.
- **TABLES**: Comma-separated list of tables to be updated.

### Payload Structure
Each type of payload will follow a structure based on the use case (see examples above). The Lambda function will inspect the payload to decide which database table to update.

### SQS Integration
- **Event Source**: The Lambda function is triggered by messages from SQS.
