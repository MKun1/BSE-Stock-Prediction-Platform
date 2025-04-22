// Populate the stock code text input when a dropdown option is selected
const stockDropdown = document.getElementById('stock-dropdown');
const stockSymbolInput = document.getElementById('stock-symbol');

stockDropdown.addEventListener('change', function() {
    stockSymbolInput.value = this.value; // Set the input field to the selected stock code
});