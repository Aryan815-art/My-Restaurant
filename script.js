const menu = {
  pizza: [
    { name: "Margherita", price: 299 },
    { name: "Farmhouse", price: 399 },
    { name: "Cheese Burst", price: 449 }
  ],
  burger: [
    { name: "Veg Burger", price: 199 },
    { name: "Cheese Burger", price: 249 },
    { name: "Double Patty", price: 299 }
  ],
  pasta: [
    { name: "White Sauce Pasta", price: 259 },
    { name: "Red Sauce Pasta", price: 239 },
    { name: "Cheese Pasta", price: 279 }
  ],
  sandwich: [
    { name: "Veg Sandwich", price: 149 },
    { name: "Grilled Sandwich", price: 179 },
    { name: "Cheese Sandwich", price: 199 }
  ]
};

let total = 0;
let selectedItems = [];

function showItems() {
  document.getElementById("items").innerHTML = "";
  const category = document.getElementById("category").value;

  if (!category) return;

  menu[category].forEach(item => {
    document.getElementById("items").innerHTML += `
      <label>
        <input type="checkbox"
          onchange="updateOrder('${item.name}', ${item.price}, this)">
        ${item.name} – ₹${item.price}
      </label><br>
    `;
  });
}

function updateOrder(name, price, checkbox) {
  if (checkbox.checked) {
    selectedItems.push({ name, price });
    total += price;
  } else {
    selectedItems = selectedItems.filter(item => item.name !== name);
    total -= price;
  }
  renderOrder();
}

function renderOrder() {
  const list = document.getElementById("orderList");
  list.innerHTML = "";

  selectedItems.forEach(item => {
    list.innerHTML += `<li>${item.name} – ₹${item.price}</li>`;
  });

  document.getElementById("total").innerText = total;
}

function placeOrder() {
  const name = document.getElementById("name").value;
  const phone = document.getElementById("phone").value;
  const address = document.getElementById("address").value;

  if (!name || !phone || !address || selectedItems.length === 0) {
    alert("Please fill all details and select items");
    return;
  }

  let billItems = "";
  selectedItems.forEach(item => {
    billItems += `${item.name} – ₹${item.price}<br>`;
  });

  document.getElementById("result").innerHTML = `
    <h3>✅ Order Confirmed</h3>
    <p><b>Name:</b> ${name}</p>
    <p><b>Phone:</b> ${phone}</p>
    <p><b>Address:</b> ${address}</p>
    <p><b>Items:</b><br>${billItems}</p>
    <h3>Grand Total: ₹${total}</h3>
  `;
}
