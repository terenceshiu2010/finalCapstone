# Capstone Project IV (OOP) - Shoe Inventory
This project is named Shoe Inventory System, it is an Object-Oriented Programming project written in Python. This system is used by shoe warehouse manager to mannage the inventory in the warehouse and performing the stock taking.
## Table of Contents
- [Installation](README.md#installation)
- [Usage](README.md#usage)
- [Credit](#credit)
## Installation
- Open a terminal or command prompt on user's computer
- Create a working directory, for example 'inventory'
- Change to the new created directory
excute below command
  ```
  git clone https://github.com/terenceshiu2010/finalCapstone
  ```
- it will clone the system files to the currenct directory like below
![image](https://user-images.githubusercontent.com/108268967/210893073-655f43f9-97ac-40cb-9760-d30fc1b0265a.png)
- In additional, you have to install below application/module to user's computer in order to make the system working smoothly
  - [x] Install Python 3
  - [x] Install one of IDE such as Phcharm or VS code
  - [x] Install module prettytable


## Usage
This section will describe the major functions of the system, when user launched the system, it will display the system logo 'Inventory System' and a number of functions user can select from the system.

![image](https://user-images.githubusercontent.com/108268967/210894157-24ea78c5-a69b-4e84-b30f-e0ab2ed500f0.png)

- capture_shoes

  Capture shoe function will allow user to create an new shoe object and add the created shoe object to the shoe list, user need to provide shoe details.
  - [x] country
  - [x] shoe code (uniquely identifier)
  - [x] shoe description
  - [x] cost
  - [x] quantity
  
  ![image](https://user-images.githubusercontent.com/108268967/210895172-1afa6c1f-13ac-42da-a8a1-5fd430d8f938.png)
  
- view_all

  View All function will displays all the shoe object available in the shoe list in a table.
  ![image](https://user-images.githubusercontent.com/108268967/210895541-427194ca-f7af-4955-afe5-dda35f5496ce.png)

- re_stock

  Re-Stock function will displays the lowest quantitiy of shoe in the shoe list, allow the user to restock this shoe by adding quantity to this shoe if needed.
  ![image](https://user-images.githubusercontent.com/108268967/210895830-142f43d9-f576-4ecd-a5d5-e6fa9d78ca7d.png)

- search_shoe

  Search Shoe function allows user to search a shoe object by the its shoe code, and display its details.
  ![image](https://user-images.githubusercontent.com/108268967/210896142-75291334-dede-43a2-9708-63a8dea22d84.png)


- value_per_item

  Value Per Item function displays the total value of each shoe object, as well as total value of all shoe object in the shoe list.
  ![image](https://user-images.githubusercontent.com/108268967/210896349-0e1f4be3-abb0-44df-add4-0e2ee36d5d4f.png)

- highest_qty

  Highest Quantity function displays the highest quantitiy of shoe object in the shoe list, inform user the shoe is being for sale.
  ![image](https://user-images.githubusercontent.com/108268967/211005986-8992353b-2005-499e-80e6-97267ed1dc5b.png)


- exit

  Exit function is used to quit the system when done.
  ![image](https://user-images.githubusercontent.com/108268967/210896755-d059a035-6cdd-4cd1-989c-e08af71ab832.png)


## Credit
This system is created by Chi Ming Terence Shiu

If you found any issue or having problem with this system, please email :e-mail: at terenceshiu2010@gmail.com
