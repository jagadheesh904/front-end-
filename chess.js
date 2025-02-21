let selectedPiece = null;

document.querySelectorAll('.square').forEach(square => {
  square.addEventListener('click', function () {
    if (selectedPiece) {
      // If there's already a selected piece, check if the move is valid
      if (isValidMove(selectedPiece, this)) {
        movePiece(selectedPiece, this);
        selectedPiece = null;
      }
    } else {
      // Select the piece when clicked
      selectedPiece = this;
    }
  });
});

function isValidMove(fromSquare, toSquare) {
  // Implement the rules for each piece here (e.g., pawn, knight, etc.)
  return true; // Placeholder for validation logic
}

function movePiece(fromSquare, toSquare) {
  toSquare.innerHTML = fromSquare.innerHTML;
  fromSquare.innerHTML = '';
}
