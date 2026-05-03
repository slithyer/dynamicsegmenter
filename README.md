💎 Mirasol Dynamic Segmenter
A Hybrid ML-Driven VIP Eligibility Engine
Mirasol is a customer analytics tool designed to move businesses from Mass Marketing to Precision Personalization. Using a combination of Unsupervised Machine Learning (K-Means Clustering) and Deterministic Business Rules, the system evaluates customer data to instantly determine VIP eligibility.

🚀 Key Features
Hybrid Intelligence: Combines the flexibility of Machine Learning with the reliability of hard-coded business rules (Age/Income filters).

Behavioral Clustering: Analyzes six distinct customer dimensions—Income, Age, Spending, Recency, and Household structure—to find hidden patterns.

Priority Override: Includes a "High-Net-Worth" logic layer to ensure top-tier earners are instantly recognized as Elite.

Admin Dashboard: A real-time history log to track segments and eligibility status.

🛠️ The Tech Stack
Frontend: HTML5, CSS3 (Modern, responsive UI)

Backend: Python & Flask

Machine Learning: Scikit-Learn (K-Means Clustering, StandardScaler)

Data Handling: NumPy, Pickle

🧠 The Machine Learning Logic
The core of this project is a K-Means Clustering model trained on customer behavior data.

Feature Scaling: Inputs like "Income" and "Age" are normalized using StandardScaler to ensure the model isn't biased by larger numerical ranges.

Weighted Analysis: I implemented Feature Weighting (3.0x multiplier on Income) to align the AI's mathematical distance calculation with real-world business priorities.

Clustering: The model assigns users to one of four clusters, which are then mapped to VIP tiers:

VIP Elite: High-engagement, high-value customers.

Standard VIP: Regular customers with steady engagement.

Budget/Low Engagement: Customers who do not currently meet VIP criteria.
