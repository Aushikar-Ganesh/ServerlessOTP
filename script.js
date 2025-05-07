const baseUrl = "https://vdqtb1gzed.execute-api.ap-south-1.amazonaws.com";

async function sendOTP() {
  const phone = document.getElementById("sendPhone").value;
  const messageDiv = document.getElementById("sendMessage");

  if (!phone) {
    messageDiv.innerText = "Please enter a phone number.";
    return;
  }

  try {
    const response = await fetch(`${baseUrl}/send-otp?phone=${encodeURIComponent(phone)}`, {
      method: 'GET',
      mode: 'cors'
    });

    const text = await response.text();
    messageDiv.innerText = text;
  } catch (error) {
    console.error("Send OTP Error:", error);
    messageDiv.innerText = "Failed to send OTP. Check CORS or API setup.";
  }
}

async function verifyOTP() {
  const phone = document.getElementById("verifyPhone").value;
  const otp = document.getElementById("otp").value;
  const messageDiv = document.getElementById("verifyMessage");

  if (!phone || !otp) {
    messageDiv.innerText = "Please enter both phone number and OTP.";
    return;
  }

  try {
    const response = await fetch(`${baseUrl}/verify-otp?phone=${encodeURIComponent(phone)}&otp=${encodeURIComponent(otp)}`, {
      method: 'GET',
      mode: 'cors'
    });

    const text = await response.text();
    messageDiv.innerText = text;
  } catch (error) {
    console.error("Verify OTP Error:", error);
    messageDiv.innerText = "Failed to verify OTP. Check CORS or API setup.";
  }
}
