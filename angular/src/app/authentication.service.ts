import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { SERVER_URL } from './app.component';

const httpOptions = {
  headers: new HttpHeaders({'Content-Type': 'application/json'})
};

@Injectable()
export class AuthenticationService {
  private google_auth_url = SERVER_URL + '/google/token_signin';

  constructor(private http: HttpClient) { }

  google_login() {
    return this.http.post<string>(this.google_auth_url, {}, httpOptions);
  }

  logout() {
    localStorage.removeItem('user_name');
  }
}
