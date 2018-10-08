import { TestBed } from '@angular/core/testing';

import { TopFeedService } from './top-feed.service';

describe('TopFeedService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: TopFeedService = TestBed.get(TopFeedService);
    expect(service).toBeTruthy();
  });
});
