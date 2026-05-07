<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Mindset of SN Course</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      background: radial-gradient(circle at center, #001f3f 0%, #000 100%);
      color: #fff;
      font-family: 'Poppins', sans-serif;
      text-align: center;
      overflow-x: hidden;
    }

    h1 {
      font-size: 60px;
      color: #00bfff;
      text-shadow: 0 0 20px #00bfff, 0 0 40px #00bfff;
      margin-top: 100px;
      letter-spacing: 2px;
      font-weight: 700;
    }

    h1 span {
      display: block;
      font-size: 80px;
      color: #66ccff;
      text-shadow: 0 0 30px #66ccff, 0 0 60px #66ccff;
    }

    p {
      font-size: 20px;
      color: #aeefff;
      margin: 20px auto;
      width: 80%;
      line-height: 1.6;
    }

    .btn {
      background: #00bfff;
      color: #000;
      border: none;
      padding: 15px 40px;
      border-radius: 50px;
      font-size: 22px;
      cursor: pointer;
      box-shadow: 0 0 20px #00bfff, 0 0 40px #00bfff;
      transition: 0.3s;
    }

    .btn:hover {
      background: #66ccff;
      box-shadow: 0 0 30px #66ccff, 0 0 60px #66ccff;
    }

    .bubble {
      position: absolute;
      border-radius: 50%;
      background: rgba(0, 191, 255, 0.3);
      animation: float 6s infinite ease-in-out;
    }

    @keyframes float {
      0% { transform: translateY(0); opacity: 1; }
      100% { transform: translateY(-100vh); opacity: 0; }
    }
  </style>
</head>
<body>
  <h1>Mindset of <span>SN</span> Course</h1>
  <p>Apna Instagram growth aur mindset shift start karo!  
     Join karo aur apni digital journey ko next level pe le jao.</p>
  <button class="btn" id="payBtn">Buy Now ₹499</button>

  <!-- Razorpay Integration -->
  <script src="https://checkout.razorpay.com/v1/checkout.js"></script>
  <script>
    document.getElementById('payBtn').onclick = function(e){
      var options = {
        "key": "YOUR_RAZORPAY_KEY_ID", // Razorpay Dashboard se lo
        "amount": 49900,
        "currency": "INR",
        "name": "Mindset of SN",
        "description": "Instagram Carousel Course",
        "image": "https://yourlogo.com/logo.png",
        "handler": function (response){
            alert("Payment Successful! ID: " + response.razorpay_payment_id);
        },
        "theme": {
            "color": "#00bfff"
        }
      };
      var rzp1 = new Razorpay(options);
      rzp1.open();
      e.preventDefault();
    }

    // Bubble animation generator
    for(let i=0; i<20; i++){
      let bubble = document.createElement('div');
      bubble.classList.add('bubble');
      bubble.style.width = Math.random()*40 + 'px';
      bubble.style.height = bubble.style.width;
      bubble.style.left = Math.random()*100 + 'vw';
      bubble.style.bottom = '-50px';
      bubble.style.animationDuration = (Math.random()*5 + 3) + 's';
      document.body.appendChild(bubble);
    }
  </script>
</body>
</html>
