import { Injectable } from '@angular/core';
import { SERVER_URL } from '../../app.component';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TopFeedService {
  private TOP_FEED_URL = SERVER_URL + '/top/d/';

  constructor(private http: HttpClient) {}

  getTopDebates(count: number) {
    return this.http.get<void>(this.TOP_FEED_URL + count, {});
  }
}
