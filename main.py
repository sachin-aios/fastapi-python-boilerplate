<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Mindset of SN Course</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #111;
      color: #fff;
      text-align: center;
      padding: 50px;
    }
    .btn {
      background: #00ff88;
      color: #111;
      padding: 15px 30px;
      border: none;
      border-radius: 8px;
      font-size: 18px;
      cursor: pointer;
    }
    .btn:hover {
      background: #00cc66;
    }
  </style>
</head>
<body>
  <h1>🚀 Mindset of SN Course</h1>
  <p>Apna Instagram growth aur mindset shift start karo!</p>
  <button class="btn" id="payBtn">Buy Now ₹499</button>

  <script src="https://checkout.razorpay.com/v1/checkout.js"></script>
  <script>
    document.getElementById('payBtn').onclick = function(e){
      var options = {
        "key": "YOUR_RAZORPAY_KEY_ID", // Razorpay Dashboard se lo
        "amount": 49900, // 499 INR in paise
        "currency": "INR",
        "name": "Mindset of SN",
        "description": "Instagram Carousel Course",
        "image": "https://yourlogo.com/logo.png",
        "handler": function (response){
            alert("Payment Successful! ID: " + response.razorpay_payment_id);
        },
        "prefill": {
            "name": "Customer Name",
            "email": "customer@email.com",
            "contact": "9999999999"
        },
        "theme": {
            "color": "#00ff88"
        }
      };
      var rzp1 = new Razorpay(options);
      rzp1.open();
      e.preventDefault();
    }
  </script>
</body>
</html>
