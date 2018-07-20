import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from '../authentication.service';

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
    let result = this.authenticationService.google_login().subscribe(
      data => console.log(data),
      error => console.log(error)
    );
    console.log(result);
  }

}
