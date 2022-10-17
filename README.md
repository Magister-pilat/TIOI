# TIOI LR1 Подсказка:
<p>  В папке LR1 присутствуют несколько файлов: generate_and_evaluate.py, my_function.py, Dockerfile, test.py, pyl.py и lab1.py.</p> 
<p>  В файле generate_and_evaluate.py содержатся исходные функции генерации правил и фактов.</p> 
<p>  В файле my_function.py содержатся функции interim_results и results, возвращающие соответственно промежуточные результаты применения правил к фактам без обработки исключения и правила, прошедшие через исключения.</p>
<p>  В файле Dockerfile описана инструкция для Dockerfile, необходимая для построения соответсвующего docker-образа.</p>
<p>  В файле test.py опсан код, необходимый для тестирования и измерния скорости работы функции генерации правил<strong>(На текущий момент данная версия программы не актуальна!).</strong></p>
<p>  В файле pyl.py опсан код функции генерации правил results() <strong>для его тестирования  анализатором Pylint</strong>.</p>
<p>  В файле lab1.py опсан код, необходимый для тестирования и измерния скорости работы функции генерации правил<strong>(На текущий момент данная версия программы является актуальной!).</strong></p>
<h3>Подсказка для файла pyl.py:</3>
<p>В файле pyl.py опсан код функции генерации правил results(), котрая принимает на вход 2 параметра: facts - список фактов, сгенерированных функцией generate_rand_facts(), и список правил, сгенерированный функцией generate_simple_rules()</p>
<h3>Подсказка для Docker:</h3> 
<p>Для создания Docker-образа необходимо в командной строке прописать следующие команды: </p>
<blockquote> sudo docker build -t name .</blockquote>
<p>где &quot;name&quot; это имя, которое Вы хотите задать Docker-образу, а &quot;.&quot; это каталог в котором расположен Ваш Dockerfile. </p>
<p>Для запуска Вашего Docker-образа необходимо в командной строке прописать следующие команды:</p>
<blockquote> sudo docker run  name </blockquote>
<p>где &quot;name&quot; это имя, которое Вы задали Docker-образу. </p>
<h3>Результаты замеров времени работы программы в секундах:</h3>
<table>
    <thead>
        <tr>
          <th>Замер №1</th>
          <th>Замер №2</th>
          <th>Замер №3</th>
          <th>Замер №4</th>
          <th>Замер №5</th>
          <th>Замер №6</th>
          <th>Замер №7</th>
          <th>Замер №8</th>
          <th>Замер №9</th>
          <th>Замер №10</th>
        </tr>
    </thead>
    <tbody>
        <tr>
          <td>22.055454</td>
          <td>22.518143</td>
          <td>21.964378</td>
          <td>23.454919</td>
          <td>23.749656</td>
          <td>22.869935</td>
          <td>22.163739</td>
          <td>25.028415</td>
          <td>25.455435</td>
          <td>22.473807</td>
        </tr>
    </tbody>
</table>
<p>И того среднее время работы программы в секундах: 23.17</p>
