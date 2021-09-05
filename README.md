<h1><samp>InventoryManagement-JSON </samp></h1>
 A typical command line inventory management using Python (JSON based)
 
<h2><samp>How to Begin ?</samp></h2>
  There are mainly two interfaces:
  <ol>
   <li>For the Worker - ServerSide</li>
   <li>For the customer - CustomerSide </li>
 </ol>
 And the JSON files being generated/used are:
 <ol>
   <li>inventory.json - To keep track of all the products (includes those which are out of stock too)</li>
   <li>outOfStock.json - To keep track of the products out of Stock</li>
   <li>sales.json - Details of each bill generated </li>
   <li>productSales.json - Each product sale descripion </li>
 </ol>
 
<h2><samp>ServerSide</samp></h2>
 Allows the worker to update the stock, as well add new products.
 Operates on 'inventory.json' file
 
<h2><samp>ClientSide</samp></h2>
 Lists out all the Available products to the user, allowing them to buy the products and generates bill.
 Operates on all the JSON files mentioned above.
 
<h2><samp>Definitions</samp></h2>
 <h4><samp>inventory.json</samp></h4>
 
 ```json
{
    "ProductID": {
        "name": ,
        "price": ,
        "quantity": 
    }
   
 }
```

 <h4><samp>outOfStock.json</samp></h4>
 
  ```json
{
    "ProductID DD/MM/YYYY HH:MM": {
        "name": ,
        "price":,
        "TimeDetail": "
    }
}
```

 <h4><samp>sales.json</samp></h4>
 
  ```json
{
    " DD/MM/YYYY HH:MM:SS": {
        "ProductID1": {
            "Qn": ,
            "total_price":,
            "name": 
        },
        "ProductID2": {
            "Qn": ,
            "total_price":,
            "name":
        }
    }
}
```

 <h4><samp>productSales.json</samp></h4>
 
  ```json
{
    "ProductID DD/MM/YYYY HH:MM": {
        "Qn": ,
        "total_price": ,
        "name": 
    }
}
```

