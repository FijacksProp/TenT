document.addEventListener('DOMContentLoaded', function() {
    const likeButtons = document.querySelectorAll('.like-button');
    const commentButtons = document.querySelectorAll('.comment-button');

    likeButtons.forEach((button, index) => {
        let likeCount = 0;
        button.addEventListener('click', function() {
            likeCount++;
            const likeCountSpan = button.nextElementSibling;
            likeCountSpan.textContent = `${likeCount} Likes`;
        });
    });

    commentButtons.forEach((button, index) => {
        button.addEventListener('click', function() {
            const commentInput = button.previousElementSibling;
            const commentText = commentInput.value.trim();
            if (commentText) {
                const commentList = button.parentElement.querySelector('.comment-list');
                const newComment = document.createElement('li');
                newComment.textContent = commentText;
                commentList.appendChild(newComment);
                commentInput.value = ''; // Clear the input
            }
        });
    });
});
