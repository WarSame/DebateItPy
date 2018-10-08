import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TopGeneralFeedComponent } from './top-general-feed.component';

describe('TopGeneralFeedComponent', () => {
  let component: TopGeneralFeedComponent;
  let fixture: ComponentFixture<TopGeneralFeedComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TopGeneralFeedComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TopGeneralFeedComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
