// Файл static/js/scripts.js

document.addEventListener('DOMContentLoaded', function() {
    var submitButton = document.getElementById('submit-button');
    var trueButton = document.getElementById('true-button');
    var falseButton = document.getElementById('false-button');

    document.getElementById('id_image').onchange = function(event) {
        var reader = new FileReader();
        reader.onload = function(){
            var imgPreview = document.getElementById('imgPreview');
            imgPreview.style.display = 'block';
            imgPreview.src = reader.result;
        };
        reader.readAsDataURL(event.target.files[0]);

        submitButton.style.display = 'block';

        var fileLabel = document.querySelector('.custom-file-upload');
        fileLabel.textContent = 'Обрати інше фото';

        removeFeedbackMessage();
        document.getElementById('classification-result').style.display = 'none';
        document.getElementById('verification-buttons').style.display = 'none';
    };

    submitButton.onclick = function() {
        var form = document.getElementById('uploadForm');
        var formData = new FormData(form);
        var imageUploadUrl = document.getElementById('image-upload-url').dataset.url;

        fetch(imageUploadUrl, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            var categoryResult = document.getElementById('category-text');
            categoryResult.textContent = "Ваше фото належить до категорії " + data.category + ".";
            document.getElementById('image-id').value = data.image_id;
            document.getElementById('image-category').value = data.category;
            document.getElementById('classification-result').style.display = 'block';
            document.getElementById('verification-buttons').style.display = 'block';
            submitButton.style.display = 'none';
            var fileLabel = document.querySelector('.custom-file-upload');
            fileLabel.textContent = 'Обрати інше фото';
        })
        .catch(error => console.error('Error:', error));
    };

    trueButton.addEventListener('click', function() {
        sendFeedback(true);
        updateUIAfterFeedback();
    });

    falseButton.addEventListener('click', function() {
        sendFeedback(false);
        updateUIAfterFeedback();
    });

    function sendFeedback(isCorrect) {
        var imageId = document.getElementById('image-id').value;
        var category = document.getElementById('image-category').value;
        var saveFeedbackUrl = document.getElementById('save-feedback-url').dataset.url;

        fetch(saveFeedbackUrl, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `image_id=${imageId}&category=${category}&feedback=${isCorrect}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                console.log('Feedback sent successfully');
            }
        })
        .catch(error => console.error('Error:', error));
    }

    function updateUIAfterFeedback() {
        var verificationButtons = document.getElementById('verification-buttons');
        verificationButtons.style.display = 'none';

        var feedbackMessage = document.createElement('div');
        feedbackMessage.id = 'feedback-message';
        feedbackMessage.textContent = 'Дякуємо за відгук!';
        feedbackMessage.style.textAlign = 'center';
        feedbackMessage.style.marginTop = '10px';
        
        var classificationResult = document.getElementById('classification-result');
        classificationResult.appendChild(feedbackMessage);
    }

    function removeFeedbackMessage() {
        var feedbackMessage = document.getElementById('feedback-message');
        if (feedbackMessage) {
            feedbackMessage.remove();
        }
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
