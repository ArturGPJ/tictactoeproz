let currentPlayer = 'X';
let gameBoard = ['', '', '', '', '', '', '', '', ''];
let gameActive = true;

const winningCombos = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], // Horizontal
    [0, 3, 6], [1, 4, 7], [2, 5, 8], // Vertical
    [0, 4, 8], [2, 4, 6] // Diagonal
];

const cells = document.querySelectorAll('.cell');
const message = document.getElementById('message');

const checkWinner = () => {
    for (let combo of winningCombos) {
        if (
            gameBoard[combo[0]] &&
            gameBoard[combo[0]] === gameBoard[combo[1]] &&
            gameBoard[combo[0]] === gameBoard[combo[2]]
        ) {
            message.innerText = `${currentPlayer} venceu!`;
            gameActive = false;
            return;
        }
    }
    if (!gameBoard.includes('')) {
        message.innerText = 'Empate!';
        gameActive = false;
    }
};

const makeMove = (index) => {
    if (!gameActive || gameBoard[index] !== '') return;

    gameBoard[index] = currentPlayer;
    cells[index].innerText = currentPlayer;

    checkWinner();

    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
};

const resetGame = () => {
    currentPlayer = 'X';
    gameBoard = ['', '', '', '', '', '', '', '', ''];
    gameActive = true;
    message.innerText = '';
    cells.forEach(cell => cell.innerText = '');
};

cells.forEach(cell => cell.addEventListener('click', () => makeMove([...cells].indexOf(cell))));