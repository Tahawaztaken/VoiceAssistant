async function getData() {
  const response = await fetch('http://127.0.0.1:5000/get_data');
  const data = await response.json();
  console.log(data);
}