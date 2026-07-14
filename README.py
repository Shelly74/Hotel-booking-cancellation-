# Hotel Bookings Analysis Data Repository 🏨📊

Welcome to the Hotel Bookings Data Analysis Repository! This project provides an in-depth exploration of hotel booking data, revealing key patterns, cancellation behaviors, revenue insights, and actionable strategies. Whether you're a data analyst, hotel operator, or business strategist, this repo offers valuable tools and insights to optimize operations, reduce cancellations, and maximize profitability.

---

## 📁 Contents

- **Dataset:** `hotel_bookings_final.csv`  
  - A comprehensive, cleaned dataset containing detailed booking information, customer demographics, and financials.

- **Sample Data Snippet:**  
  - Example entries from the dataset illustrating the data structure and key features.

- **Analysis Notebook:**  
  - Python Jupyter Notebook comprising data cleaning, exploratory analysis, visualizations, and insights.

- **Summary Report:**  
  - An extensive document summarizing key trends, root causes, and strategic recommendations.

- **Power BI Dashboards:**  
  1. **Booking & Cancellation Insights**  
     - Visualizations on booking trends, cancellation patterns, seasonality, and channel performance.
  
  2. **Revenue & Profitability Insights**  
     - Interactive visuals showing revenue metrics, property performance, monthly and city-level insights, and maps.

---

## 🔍 Dataset Overview

The dataset `hotel_bookings_final.csv` contains 24 columns with detailed booking and customer information, including:
- Customer demographics (`customer_id`, `city`, `customer_star_rating`)
- Booking details (`booking_date`, `check_in_date`, `check_out_date`, `stay_type`, `num_rooms_booked`)
- Property details (`property_id`, `room_type`, `star_rating`)
- Financials (`selling_price`, `payment_method`, `refund_status`, `refund_amount`)
- Booking channel and status (`channel_of_booking`, `booking_status`)
- Additional info (`cancellation_flag`, `booking_month`, `season`, etc.)

This structured dataset allows for granular analysis of booking behaviors, cancellation patterns, revenue streams, and seasonal impacts.

---

## 📝 Sample Data & Example Entries

Below is a sample subset from the dataset to illustrate the data structure and key features:

| customer_id | property_id | city           | star_rating | booking_date | check_in_date | check_out_date | room_type | stay_type | selling_price | payment_method | refund_status | refund_amount | channel_of_booking | booking_status | travel_date | cashback | coupon_redeem | Coupon_Used? |
|--------------|--------------|----------------|-------------|--------------|--------------|--------------|-----------|-----------|--------------|----------------|--------------|--------------|-------------------|----------------|--------------|----------|--------------|--------------|
| 492          | 3            | San Francisco  | 4           | 2024-04-01   | 2024-05-24   | 2024-05-26   | Standard  | Leisure   | 25342        | PayPal         | Yes          | 369.65       | Web                | Confirmed      | 2024-03-04  | 5.37     | 0.00         | No           |
| 180          | 3            | Dallas         | 3           | 2024-04-01   | 2024-05-10   | 2024-05-17   | Deluxe    | Leisure   | 8033         | Bank Transfer  | Yes          | 492.51       | Web                | Confirmed      | 2024-07-19  | 7.16     | 0.00         | No           |
| 50           | 5            | Dallas         | 3           | 2024-04-01   | 2024-05-31   | 2024-06-05   | Deluxe    | Business  | 29715        | Debit Card     | Yes          | 0.00         | iOS                | Confirmed      | 2024-03-22  | 0.00     | 0.00         | No           |
| 294          | 3            | Orlando        | 4           | 2024-04-01   | 2024-04-18   | 2024-04-24   | Deluxe    | Leisure   | 44592        | Bank Transfer  | Yes          | 545.54       | Android            | Confirmed      | 2024-11-24  | 7.93     | 24.50        | Yes          |
| 40           | 5            | Seattle        | 5           | 2024-04-01   | NaN          | NaN          | Deluxe    | Leisure   | 15873        | Debit Card     | Yes          | 211.37       | Web                | Cancelled      | 2024-03-02  | 0.00     | 0.00         | No           |

*Note:* The dataset includes missing values (e.g., NaN for check-in/check-out dates), which are handled during data cleaning.

---

## 📊 Analysis & Insights

### 1. Key Trends & Patterns

#### **Room Type & Cancellation Behavior**
- Standard rooms exhibit the highest cancellation rate (~23.3%), indicating budget-conscious customers tend to cancel more.
- Deluxe and Suite rooms show lower cancellation rates (~16-17.98%), reflecting higher commitment levels.
- **Implication:** Pricing sensitivity influences cancellation; premium rooms attract more committed guests.

#### **Star Rating & Property Value**
- 5-star properties have slightly higher cancellation rates (~21.3%) compared to 2-4 stars (~20%).
- High-value bookings may have flexible plans or last-minute changes.

#### **Seasonality & Temporal Patterns**
- Booking volume peaks in April (~4,494 bookings), with low-demand months like February, June, and September (~2,200 bookings).
- Highest cancellations occur in July (~30.33%), August (~28.77%), and December (~25.76%), likely due to holiday travel.
- Off-peak months (April, November) see more stable booking behavior with lower cancellations (~15-16%).

#### **Booking Channels & Coupon Usage**
- Web, iOS, and Android channels have similar cancellation rates (~20%), indicating channel choice doesn't significantly influence cancellations.
- Bookings with coupons show marginally higher cancellations (~20.8%) versus non-coupon bookings (~20.1%).

### 2. Root Cause Analysis
- **Price Sensitivity:** Lower-cost standard rooms and coupon-based bookings are more cancellation-prone.
- **Property & Purpose:** Premium property bookings (Deluxe/Suite) tend to be more stable, possibly due to purpose-driven travel or higher commitment.
- **Seasonality:** Peak months experience elevated cancellations, likely due to increased booking volume and flexible travel plans.

### 3. Business Impact & Opportunities
- Focus on high-risk segments such as standard rooms and coupon users.
- Promote premium rooms and loyalty programs to enhance commitment.
- Adjust pricing strategies seasonally, offering incentives during off-peak months.
- Implement prepayment policies during peak seasons to reduce last-minute cancellations.

---

## 💡 Business Recommendations

### **Reducing Cancellations**
- **Prepayment & Deposits:** Implement partial prepayment for high-risk bookings to secure commitments.
- **Reminders & Incentives:** Send automated reminders, confirmation emails, or small incentives to encourage adherence.
- **Targeted Promotions:** Offer early-booking discounts for premium rooms or loyal customers.

### **Enhancing Profitability**
- **Promote Premium & Longer Stays:** Upsell higher-star properties and encourage extended bookings.
- **Loyalty & Personalization:** Use loyalty programs and personalized offers to retain customers.
- **Dynamic Pricing:** Adjust room rates based on demand, seasonality, and booking lead time.

### **Channel & Seasonal Strategies**
- **Channel Focus:** Since cancellation rates are similar across channels, prioritize high-volume channels for marketing.
- **Seasonal Campaigns:** Run targeted promotions during low-demand months and flexible policies during peak seasons.

---

## 🚀 Power BI Dashboards & Visualizations

### **1. Booking & Cancellation Insights Dashboard**
- Trends by room type, star rating, booking channel, and seasonality.
- Monthly booking volumes and cancellation patterns.
- City-level booking and cancellation maps.

### **2. Revenue & Profitability Dashboard**
- Total and average revenue metrics.
- Revenue by property type, city, and month.
- Visualizations of high-performing hotels and seasonal revenue fluctuations.

---

## 🛠️ Tools & Technologies Used
- **Python:** Data cleaning, analysis, and visualization with Pandas, Matplotlib, Seaborn.
- **Power BI:** Interactive dashboards for real-time insights.
- **CSV Dataset:** Preprocessed with necessary transformations for analysis.

---

## 🎉 Final Note
This analysis provides a comprehensive understanding of hotel booking behaviors. By focusing on high-risk segments, seasonality, and strategic pricing, your business can significantly reduce cancellations and improve revenue streams.

Thank you for exploring this project! 🌟

---

# Author 
Name : Shelly Garg 

