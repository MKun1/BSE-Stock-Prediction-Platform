
document.getElementById('stock-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    const stockSymbolInput = document.getElementById('stock-symbol');
    const errorMessage = document.getElementById('error-message');

    // Example validation: Check if stock code matches known codes
    const validStockCodes = [
  'RELIANCE',    // Reliance Industries
  'TCS',         // Tata Consultancy Services
  'HDFCBANK',    // HDFC Bank
  'ICICIBANK',   // ICICI Bank
  'INFY',        // Infosys
  'HINDUNILVR',  // Hindustan Unilever
  'ITC',         // ITC Ltd
  'BHARTIARTL',  // Bharti Airtel
  'SBIN',        // State Bank of India
  'LT',          // Larsen & Toubro
  'KOTAKBANK',   // Kotak Mahindra Bank
  'AXISBANK',    // Axis Bank
  'BAJFINANCE',  // Bajaj Finance
  'ASIANPAINT',  // Asian Paints
  'M&M',         // Mahindra & Mahindra
  'SUNPHARMA',   // Sun Pharma
  'MARUTI',      // Maruti Suzuki
  'TATAMOTORS',  // Tata Motors
  'NESTLEIND',   // Nestlé India
  'BAJAJFINSV',  // Bajaj Finserv
  'POWERGRID',   // Power Grid Corp
  'NTPC',        // NTPC
  'ULTRACEMCO',  // UltraTech Cement
  'TITAN',       // Titan Company
  'ADANIENT',    // Adani Enterprises
  'ADANIPORTS',  // Adani Ports
  'WIPRO',       // Wipro
  'HCLTECH',     // HCL Technologies
  'TECHM',       // Tech Mahindra
  'INDUSINDBK',  // IndusInd Bank
  'GRASIM',      // Grasim Industries
  'JSWSTEEL',    // JSW Steel
  'TATASTEEL',   // Tata Steel
  'BAJAJ-AUTO',  // Bajaj Auto
  'BRITANNIA',   // Britannia
  'CIPLA',       // Cipla
  'DRREDDY',     // Dr. Reddy's
  'EICHERMOT',   // Eicher Motors
  'HEROMOTOCO',  // Hero MotoCorp
  'HINDALCO',    // Hindalco
  'ONGC',        // ONGC
  'COALINDIA',   // Coal India
  'BPCL',        // BPCL
  'IOC',         // Indian Oil Corp
  'GAIL',        // GAIL
  'DIVISLAB',    // Divi's Labs
  'SBILIFE',     // SBI Life Insurance
  'HDFCLIFE',    // HDFC Life Insurance
  'ICICIPRULI',  // ICICI Prudential Life
  'TATACONSUM',  // Tata Consumer
  'VEDL',        // Vedanta Ltd
  'UPL',         // UPL Ltd
  'SHREECEM',    // Shree Cement
  'DABUR',       // Dabur India
  'GODREJCP',    // Godrej Consumer
  'ZEEL',        // Zee Entertainment
  'AMBUJACEM',   // Ambuja Cements
  'ACC',         // ACC Ltd
  'DLF',         // DLF Ltd
  'TATAPOWER',   // Tata Power
  'SIEMENS',     // Siemens Ltd
  'BOSCHLTD',    // Bosch Ltd
  'INFRATEL',    // Bharti Infratel
  'LUPIN',       // Lupin Ltd
  'AUROPHARMA',  // Aurobindo Pharma
  'ZYDUSLIFE',   // Zydus Lifesciences
  'BIOCON',      // Biocon
  'GLENMARK',    // Glenmark Pharma
  'PIDILITIND',  // Pidilite Industries
  'COLPAL',      // Colgate-Palmolive
  'BERGEPAINT',  // Berger Paints
  'HAVELLS',     // Havells India
  'MOTHERSUMI',  // Motherson Sumi
  'ASHOKLEY',    // Ashok Leyland
  'BHARATFORG',  // Bharat Forge
  'TATACHEM',    // Tata Chemicals
  'INDHOTEL',    // Indian Hotels (Taj)
  'PETRONET',    // Petronet LNG
  'MUTHOOTFIN',  // Muthoot Finance
  'PAGEIND',     // Page Industries (Jockey)
  'JUBLFOOD',    // Jubilant FoodWorks (Domino’s)
  'NAUKRI',      // Info Edge (Naukri)
  'BANDHANBNK',  // Bandhan Bank
  'FEDERALBNK',  // Federal Bank
  'IDFCFIRSTB',  // IDFC First Bank
  'YESBANK',     // Yes Bank
  'PNB',         // Punjab National Bank
  'BANKBARODA',  // Bank of Baroda
  'CANBK',       // Canara Bank
  'UNIONBANK',   // Union Bank
  'LICHSGFIN',   // LIC Housing Finance
  'CHOLAFIN',    // Cholamandalam Finance
  'SRTRANSFIN',  // Shriram Transport Finance
  'ADANIGREEN',  // Adani Green Energy
  'ADANITRANS',  // Adani Transmission
  'TATACOMM',    // Tata Communications
  'IDEA',        // Vodafone Idea
  'BHEL',        // Bharat Heavy Electricals
  'NMDC',        // NMDC Ltd
  'SAIL'         // Steel Authority of India (SAIL)
];
    if (!validStockCodes.includes(stockSymbolInput.value.toUpperCase())) {
        errorMessage.style.display = 'block'; // Show error message
    } else {
        errorMessage.style.display = 'none'; // Hide error message
        // Proceed to backend interaction (e.g., API call)
        console.log('Valid stock code submitted:', stockSymbolInput.value);
    }
    });