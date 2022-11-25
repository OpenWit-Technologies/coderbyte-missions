import $ from 'jquery'

const rootApp = document.getElementById('root')
rootApp.innerHTML = `<div id="mainArea">
  <p>button count: <span id='btncount'>0</span></p>
  <button id="mainButton" onClick="increment()">Increase</button>
</div>`
var count = 0
var button = document.getElementById('mainButton')
var number = document.getElementById('btncount')

button.onclick = function () {
  count += 1
  number.innerHTML = count
}
