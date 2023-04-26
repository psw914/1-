

// 공통
let elNav = document.querySelector("header > ul");
let datas = document.querySelectorAll("main > section");
const title = document.querySelectorAll(".hn li")
let curIdx = 0;

function handleClick(event) {
  // div에서 모든 "click" 클래스 제거
  title.forEach((e) => {
    e.classList.remove("clicked");
  });
  // 클릭한 div만 "click"클래스 추가
  event.target.classList.add("clicked");
}

title.forEach((e) => {
  e.addEventListener("click", handleClick);
});

function doScroll(sidx) {
  sidx = sidx < 0 ? 0 : sidx;
  sidx = sidx > datas.length - 1 ? datas.length - 1 : sidx;

  curIdx = sidx;

  datas[curIdx].scrollIntoView({
    block: "start", inline: "start", behavior: "smooth"
  });
}


Array.from(elNav.children, function (elMenu, idx, elMenus) {


  elMenu.addEventListener("click", function () {

    // const clickedClass = "clicked";
    // if(elMenu.classList.contains(clickedClass)){
    //   elMenu.classList.remove(clickedClass);
    // } else {
    //   elMenu.classList.add(clickedClass);
    // }


    doScroll(idx);
  });

});








// *************************11111111111111111111

const ctx = document.getElementById('myChart1');
console.log(data1996)

new Chart(ctx, {
  type: 'bar',
  data: {
    labels: [
      {% for i in data1996 %} "{{i.cook_name}}", {% endfor %}
    ],
    datasets: [{
      label: '# of',
      data: [
        {% for i in data1996 %} {{i.unit_price}}, {% endfor %}
      ],
    }]
  },
  options: {
    responsive: false,
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});



//--------------------------------- subBox2
const ctx2 = document.getElementById('myChart2');
const DATA_COUNT = 5;
const NUMBER_CFG = {count: DATA_COUNT, min: 0, max: 100};

new Chart2(ctx2, {
  type: 'pie',
  data: {
    labels: [
      'Red',
      'Blue',
      'Yellow'
    ],
    datasets: [{
      label: 'First',
      data: [300, 50, 100],
      // data: Utils.numbers(NUMBER_CFG),
      backgroundColor: [
        'rgb(90, 90, 90)',
        'rgb(54, 162, 235)',
        'rgb(255, 205, 86)'
      ],
      borderColor:["rgb(234, 234, 234)"],
      hoverOffset: 4
    }]
  },
  options: {
    responsive: false,
    pieceLabel: {
      mode:"label",
      position:"default",
      fontSize: 11,
      fontStyle: "bold",
   },
    plugins: {
      legend: {
        display: false
      },
    }

  }
});


// 22222222222222222222222
