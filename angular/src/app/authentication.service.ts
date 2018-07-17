import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class AuthenticationService {

  constructor(private http: HttpClient) { }

  google_login() {
    return this.http.post('${SERVER_URL}/test', {});
  }

  logout() {
    localStorage.removeItem('user');
  }
}
