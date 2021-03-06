import { Injectable } from '@angular/core';
import { SERVER_URL } from '../../app.component';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TopFeedService {
  private TOP_FEED_URL = SERVER_URL + '/api/top/d/';
  private TAILORED_FEED_URL = SERVER_URL + '/tailored/d';

  constructor(private http: HttpClient) {}

  getTopDebates(count: string) {
    return this.http.get<void>(this.TOP_FEED_URL + count, {});
  }
}
