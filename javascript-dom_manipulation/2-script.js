document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('red_header').addEventListener('click', function () {
    document.querySelector('header').classList.add('red');
  });
});
