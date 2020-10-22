

function makeGrid(row, col) {
    const tBody = document.createElement('tbody');
    document.querySelector('#pixelCanvas').appendChild(tBody);
    for (let i = 0; i < row; i++) {
        const tr = document.createElement('tr');
        tBody.appendChild(tr)
        for (let y = 0; y < col; y++) {
            const td = tr.appendChild(document.createElement('td'));
            td.addEventListener('click', function () {
                let color = document.getElementById("colorPicker").value;
                td.setAttribute('style', "background : " + color);
            });
        }
    }
};



document.addEventListener('submit', function (event) {
    const row = document.getElementById("inputHeight").value;
    const col = document.getElementById("inputWidth").value;
    document.querySelector('#pixelCanvas').innerHTML = '';
    makeGrid(row, col);
    event.preventDefault();
});


makeGrid(20, 20);


