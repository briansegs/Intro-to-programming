// Select color input
// Select size input

// When size is submitted by the user, call makeGrid()

function makeGrid() {

// Your code goes here!

}
const r = 20;
const c = 20;

const tBody = document.createElement('tbody');
document.querySelector('#pixelCanvas').appendChild(tBody);
for (let i = 0; i < r; i++) {
    const tr = document.createElement('tr');
    // tr.setAttribute('class', 'test');
    tBody.appendChild(tr)
    for (let y = 0; y < c; y++) {
        const td = tr.appendChild(document.createElement('td'));
        td.addEventListener('click', function () {
            console.log('Click!');
            let color = document.getElementById("colorPicker").value;
            td.setAttribute('style', "background : " + color);
        });
    }
}


function makeRow() {
    const tBody = document.querySelector('tbody');
    var tr = document.createElement('tr');
    var td = document.createElement('td');
    tr.setAttribute('class', 'test');
    tr.appendChild(td);
    tBody.appendChild(tr)
}

