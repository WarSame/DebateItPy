import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from '../../services/authentication/authentication.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  constructor(public authenticationService: AuthenticationService) {
    this.authenticationService = authenticationService;
  }

  ngOnInit() {}

  authenticate() {
    this.authenticationService.google_login().subscribe(
      data => {
        console.log(data);
        localStorage.setItem('user_name', data);
      },
      error => {
        console.log(error);
        console.log(error.error);
      }
    );
  }

}
