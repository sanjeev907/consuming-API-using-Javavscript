const form = document.querySelector('form');
const url = 'http://127.0.0.1:8000/post/';


function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
      return parts.pop().split(';').shift();
    }
  }
  form.addEventListener('submit', (e) => {
    e.preventDefault(); // prevent the default form submission behavior
    
    // get the input values
    const name = form.elements['name'].value;
    const age = form.elements['age'].value;
    const test = form.elements['test'].value;
    const B2B_price = form.elements['B2B_price'].value;
    const status = form.elements['status'].value;
    const B2C_price = form.elements['B2C_price'].value;
    const B2C_Status = form.elements['B2C_Status'].value;
      
      // create the data object to send in the request body
    const data = { name, age, test, B2B_price, status, B2C_price, B2C_Status};
    
    // get the CSRF token value
    const csrfToken = getCookie('csrftoken');
    
    // send the request using the Fetch API, including the CSRF token in the headers
    fetch(url, {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      }
    })
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Network response was not ok.');
      }
    })
    .then(data => {
      console.log(data); // log the response data to the console

    form.elements['name'].value = '';
    form.elements['age'].value = '';
    form.elements['test'].value = '';
    form.elements['B2B_price'].value = '';
    form.elements['status'].value = '';
    form.elements['B2C_price'].value = '';
    form.elements['B2C_Status'].value = '';
    })
    .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
    });
  });