// const { createPool } = require('mysql');


// const pool = createPool({
//     host:"localhost",
//     user:"root",
//     password:"pranav@28",
//     database:"dumb",
//     connectionLimit:5
// })

// pool.query("select * from basicconcept_text",(error,result,fields)=>{
//     if(error){
//         return console.log("Error : ",error);
//     }
//     return console.log(result);
// })



// ==============================================
const { createPool } = require('mysql');

const pool = createPool({
    host: "localhost",
    user: "root",
    password: "pranav@28",
    database: "dumb",
    connectionLimit: 5
});

pool.query("SELECT * FROM basicconcept_text", (error, result, fields) => {
    if (error) {
        return console.log("Error: ", error);
    }

    // Assuming the first row is English and the second row is Marathi
    const eng = result[0].action;
    const mar = result[1].action;

    // Update HTML elements with the retrieved data
    document.getElementById('eng').innerText = eng;
    document.getElementById('mar').innerText = mar;
    console.log(eng);
    console.log(mar);
});







// const mysql = require('mysql');

// // MySQL database configuration
// const dbConfig = {
//   host: 'localhost',
//   user: 'root',
//   password: 'pranav@28',
//   database: 'dumb',
// };

// // Create a MySQL connection
// const connection = mysql.createConnection(dbConfig);

// // Connect to the database
// connection.connect();

// // MySQL query to fetch English and Marathi text
// const sqlQuery = 'SELECT id, action FROM text WHERE id IN (1, 2)';

// // Execute the query
// connection.query(sqlQuery, (error, results) => {
//   if (error) {
//     console.error('Error fetching data:', error);
//     connection.end(); // Close the connection in case of an error
//     return;
//   }

//   // Assuming results[0] corresponds to English text and results[1] to Marathi text
//   const englishText = results[0].action;
//   const marathiText = results[1].action;

//   // Update HTML content
//   const englishTranslator = document.querySelector('.english-translator');
//   const marathiTranslator = document.querySelector('.marathi-translator');
//   englishTranslator.textContent = `English Sentence: ${englishText}`;
//   marathiTranslator.textContent = `Marathi Sentence: ${marathiText}`;

//   // Close the connection
//   connection.end();
// });

