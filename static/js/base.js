
// code for saving recipes with the heart icon

document.querySelectorAll('.recipes-heart-icon').forEach(icon => {
    icon.addEventListener('click', function(e) {
        e.preventDefault();
        const recipeId = this.dataset.recipeId;
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/save-recipe/', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.setRequestHeader('X-CSRFToken', csrfToken);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    const data = JSON.parse(xhr.responseText);
                    if (data.status === 'success') {
                        // Update UI to reflect saved/unsaved state
                        if (icon.classList.contains('saved')) {
                            icon.classList.remove('saved');
                        } else {
                            icon.classList.add('saved');
                        }
                    }
                } else {
                    console.error('Error:', xhr.status);
                }
            }
        };
        xhr.send(JSON.stringify({ recipe_id: recipeId }));
    });
});
