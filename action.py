#!/usr/bin/env python
# -*- coding: utf-8 -*-


print"""
<!DOCTYPE HTML>
<html>
	<head>
		<title>Serre Bot Couarch</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
		<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
	</head>
	<body class="is-preload">

		<!-- Wrapper -->
			<div id="wrapper" class="fade-in">
				<!-- Header -->
					<header id="header">
						<a href="index.html" class="logo">Bot Couarch</a>
					</header>

				<!-- Nav -->
					<nav id="nav">
						<ul class="links">
							<li><a href="index.py">Capteurs</a></li>
							<li class="active"><a href="action.py">Actionneurs</a></li>
							<li><a href="configuration.py">Configuration</a></li>
						</ul>
						<ul class="icons">
							<li><a href="https://www.facebook.com/PierreRabhiofficiel/" class="icon brands fa-facebook-f"><span class="label">Facebook</span></a></li>
							<li><a href="https://github.com/Julien-LM/green_house_monitoring" class="icon brands fa-github"><span class="label">GitHub</span></a></li>
						</ul>
					</nav>

				<!-- Main -->
					<div id="main">

						<section class="post">
						<!-- Fenêtre -->
							<h2>Fenêtre Serre</h2>

							<div class="table-wrapper">
								<table>
									<tbody>
										<tr>
											<td>La fenêtre est actuellement</td>
											<td>XXXX</td>
										</tr>
									</tbody>
								</table>
							</div>

							<div class="row gtr-uniform">
								<p>Temps d'ouverture de la fenêtre: </p>
								<div class="col-6 col-12-xsmall">
									<input type="text" name="demo-name" id="demo-name" value="" placeholder="En minutes" />
								</div>
							</div>
								<ul class="actions">
									<li><a href="#" class="button primary">Fermer</a></li>
									<li><a href="#" class="button">Ouvrir</a></li>
								</ul>
							<hr />

							<h2>Arrosage Serre</h2>

							<div class="table-wrapper">
								<table>
									<tbody>
										<tr>
											<td>L'arrosage est actuellement</td>
											<td>XXXX</td>
										</tr>
									</tbody>
								</table>
							</div>

							<div class="row gtr-uniform">
								<p>Temps d'arrosage de la serre: </p>
								<div class="col-6 col-12-xsmall">
									<input type="text" name="demo-name" id="demo-name" value="" placeholder="En minutes" />
								</div>
							</div>
								<ul class="actions">
									<li><a href="#" class="button primary">Eteindre</a></li>
									<li><a href="#" class="button">Allumer</a></li>
								</ul>
							<hr />


						</section>
					</div>



				<!-- Footer -->
					<footer id="footer">
						<section>
							<form method="post" action="#">
								<div class="fields">
									<div class="field">
										<label for="name">Name</label>
										<input type="text" name="name" id="name" />
									</div>
									<div class="field">
										<label for="email">Email</label>
										<input type="text" name="email" id="email" />
									</div>
									<div class="field">
										<label for="message">Message</label>
										<textarea name="message" id="message" rows="3"></textarea>
									</div>
								</div>
								<ul class="actions">
									<li><input type="submit" value="Send Message" /></li>
								</ul>
							</form>
						</section>
						<section class="split contact">
							<section class="alt">
								<h3>Adresse</h3>
								<p>Vallée verdoillante de Bot Couarch<br />
								Paradise City, Breizh</p>
							</section>
							<section>
								<h3>Phone</h3>
								<p><a href="#">06.76.77.80.35</a></p>
							</section>
							<section>
								<h3>Email</h3>
								<p><a href="#">julien.lemellec@gmail.com</a></p>
							</section>
							<section>
								<h3>Social</h3>
								<ul class="icons alt">
									<li><a href="https://www.facebook.com/PierreRabhiofficiel/" class="icon brands alt fa-facebook-f"><span class="label">Facebook</span></a></li>
									<li><a href="https://github.com/Julien-LM/green_house_monitoring" class="icon brands alt fa-github"><span class="label">GitHub</span></a></li>
								</ul>
							</section>
						</section>
					</footer>

				<!-- Copyright -->
					<div id="copyright">
						<ul><li>&copy; Bot Couarch Inc.</li><li>Design by: <a href="https://github.com/Julien-LM/green_house_monitoring">le T5</a></li></ul>
					</div>

			</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.scrollex.min.js"></script>
			<script src="assets/js/jquery.scrolly.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>
"""